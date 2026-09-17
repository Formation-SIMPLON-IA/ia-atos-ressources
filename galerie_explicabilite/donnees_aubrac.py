"""Générateur du jeu de dossiers de crédit fictif « Crédit Aubrac ».

Utilisé par les deux notebooks de la galerie d'explicabilité. Le jeu est
entièrement synthétique et **la règle qui fabrique la cible est connue**
(cf. `REGLE_GENERATRICE`) : c'est ce qui permet de vérifier si une méthode
d'explicabilité retrouve, ou non, ce que le modèle aurait dû apprendre.

Deux choix de génération sont volontaires et documentés :

- `reference_dossier` est un **pur bruit** (un numéro de dossier). Sur un
  échantillon fini, une importance peut apparaître par hasard ; elle ne doit
  pas être stable ni améliorer matériellement la performance en validation.
- `interruption_carriere_mois` est une **variable proxy** : elle est très
  corrélée à l'attribut sensible `sexe`, qui influence lui-même le label
  (biais historique des décisions passées). La colonne `sexe` n'est pas
  donnée au modèle — c'est exactement la situation réelle.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

RANDOM_STATE = 42

REGLE_GENERATRICE = """
logit(defaut) = -3.10
    + 0.080 * (taux_endettement - 30)
    + 0.900 * nb_incidents_12m
    - 0.006 * (anciennete_emploi_mois - 60)
    - 0.000045 * (epargne_disponible - 2000)
    + 0.550 * [montant_demande / revenu_mensuel > 6]
    + 0.600 * [type_contrat == Interim]
    + 0.350 * [type_contrat == CDD]
    + 0.450 * [sexe == F]          <-- biais historique, PAS une cause
"""

COLONNES_NUMERIQUES = [
    "reference_dossier",
    "revenu_mensuel",
    "taux_endettement",
    "anciennete_emploi_mois",
    "montant_demande",
    "duree_mois",
    "epargne_disponible",
    "nb_incidents_12m",
    "interruption_carriere_mois",
]
COLONNES_CATEGORIELLES = ["type_contrat"]
COLONNE_SENSIBLE = "sexe"
CIBLE = "defaut"


def generer_dossiers(n: int = 4000, random_state: int = RANDOM_STATE) -> pd.DataFrame:
    """Génère `n` dossiers de crédit fictifs, cible `defaut` incluse.

    Args:
        n: nombre de dossiers à générer.
        random_state: graine de reproductibilité.

    Returns:
        Un DataFrame de `n` lignes contenant les variables candidates, la
        colonne sensible `sexe` (à ne PAS donner au modèle) et la cible
        binaire `defaut` (1 = incident de remboursement constaté).
    """
    rng = np.random.default_rng(random_state)

    sexe = rng.choice(["F", "H"], size=n, p=[0.48, 0.52])

    revenu = np.round(rng.lognormal(mean=7.9, sigma=0.35, size=n) / 10) * 10
    revenu = np.clip(revenu, 1200, 9000)

    # Proxy : interruption de carrière, très inégalement répartie selon le sexe.
    base_interruption = rng.gamma(shape=1.2, scale=3.0, size=n)
    interruption = np.where(
        sexe == "F", base_interruption + rng.gamma(2.0, 6.0, n), base_interruption
    )
    interruption = np.round(np.clip(interruption, 0, 60)).astype(int)

    anciennete = np.round(np.clip(rng.gamma(2.0, 30.0, n), 1, 300)).astype(int)
    montant = np.round(rng.uniform(2000, 40000, n) / 100) * 100
    duree = rng.choice([12, 24, 36, 48, 60, 72], size=n, p=[0.1, 0.2, 0.3, 0.2, 0.15, 0.05])
    epargne = np.round(np.clip(rng.lognormal(7.5, 1.1, n), 0, 60000) / 50) * 50
    incidents = rng.poisson(0.35, n)
    contrat = rng.choice(
        ["CDI", "CDD", "Interim", "Independant"], size=n, p=[0.62, 0.18, 0.08, 0.12]
    )
    reference = rng.integers(100000, 999999, n)  # pur bruit

    charge = montant / duree
    taux_endettement = np.round(
        np.clip(charge / revenu * 100 + rng.normal(12, 4, n), 3, 75), 1
    )

    logit = (
        -3.10
        + 0.080 * (taux_endettement - 30)
        + 0.900 * incidents
        - 0.0060 * (anciennete - 60)
        - 0.000045 * (epargne - 2000)
        + 0.55 * (montant / revenu > 6).astype(float)
        + 0.60 * (contrat == "Interim")
        + 0.35 * (contrat == "CDD")
        + 0.45 * (sexe == "F")
    )
    defaut = (rng.random(n) < 1 / (1 + np.exp(-logit))).astype(int)

    return pd.DataFrame(
        {
            "reference_dossier": reference,
            "revenu_mensuel": revenu,
            "taux_endettement": taux_endettement,
            "anciennete_emploi_mois": anciennete,
            "montant_demande": montant,
            "duree_mois": duree,
            "epargne_disponible": epargne,
            "nb_incidents_12m": incidents,
            "interruption_carriere_mois": interruption,
            "type_contrat": contrat,
            COLONNE_SENSIBLE: sexe,
            CIBLE: defaut,
        }
    )
