# Galerie explicabilité — expliquer une décision de modèle

> Étagère asynchrone, **optionnelle** — pas un brief, pas de livrable, pas de note.
> Utilisable dès M6, et directement mobilisable pour ton **cas d'usage certif**.

---

## À quoi ça sert

Depuis M4, tu remplis la ligne « **explicabilité** » de `grille_decision_C4.md`
et l'étape 5 de la feuille de route du cas d'usage (« tableau perf × coût ×
latence × explicabilité × biais »). Jusqu'ici tu la remplissais **de mémoire**,
sans avoir jamais produit une explication.

Cette galerie comble ce trou. Elle ancre trois gestes :

1. produire une **importance globale honnête** (et savoir pourquoi
   `feature_importances_` n'en est pas une) ;
2. produire une **explication locale** SHAP et la traduire en une phrase
   lisible par un client — le livrable réellement attendu en crédit, RH ou santé ;
3. utiliser l'explicabilité comme **outil d'audit** : détecter une variable
   proxy qui reconstruit un attribut sensible (passerelle C2 / M2-B1).

Le fil conducteur, comme partout dans le parcours : **savoir quand ce n'est pas
la peine**. Sur un modèle linéaire, l'explication est déjà là — SHAP serait du
sur-engineering.

## Les notebooks

| Notebook | Ce que tu pratiques | Autonomie | Temps |
|---|---|---|---|
| [`01_explicabilite_pas_a_pas.ipynb`](01_explicabilite_pas_a_pas.ipynb) | Le geste complet sur un jeu **dont on connaît la règle génératrice** : coefficients vs impureté vs permutation, SHAP local (waterfall, additivité, phrase client), SHAP global (beeswarm), **détection d'une variable proxy** et son coût réel, LIME en contraste | 🟢 **Résolu** | ~2 h |
| [`02_explicabilite_sur_ton_modele_TODO.ipynb`](02_explicabilite_sur_ton_modele_TODO.ipynb) | Le même geste, **sans guidage**, sur `pyrenex_risk_v2.joblib` (ton repo M6-B2) ou sur le modèle de ton cas d'usage. Que des `# TODO` + des encadrés 🧭 repères pour t'auto-vérifier | 🟠 **À toi** | ~1 h 30 |

Fais-les dans l'ordre : le 02 suppose le 01.

## Ce que tu trouveras aussi dans le dossier

- `donnees_aubrac.py` — générateur reproductible du jeu de dossiers de crédit
  fictif (`random_state=42`). Les deux pièges qu'il contient (une variable de
  bruit pur, une variable proxy) sont documentés dans son docstring : lis-le
  **après** avoir fait le notebook 01, pas avant.

## Installation

```bash
pip install -r requirements.txt
```

> ⚠️ `scikit-learn` est **figé en 1.5.\*** : le modèle `pyrenex_risk_v2.joblib`
> utilisé par le notebook 02 a été sérialisé avec cette version et refuse de se
> charger sous une version plus récente. Le plus simple reste de travailler
> depuis le venv de ton repo M6-B2 et d'y ajouter `pip install shap lime`.

Tout tourne sur CPU, en local, sans téléchargement de données.

## Fiches associées

`fiche_interpretabilite_xai.pdf` · `grille_decision_C4.md` ·
`fiche_pattern_ML_supervise.md` · `cheatsheet_metriques.md`

---

*Galerie explicabilité — étagère optionnelle, mobilisable pour le cas d'usage certif.*
