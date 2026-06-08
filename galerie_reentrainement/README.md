# Galerie de réentraînement — pour ancrer C5

> Étagère asynchrone, **optionnelle**, à utiliser quand tu veux.
> Ce n'est pas un brief, il n'y a pas de livrable obligatoire.

---

## À quoi ça sert

Tu as fait M1-B1 (Pyrenex) sur un seul cas. Le geste « entraîner un modèle »
ne s'ancre vraiment qu'en le **rejouant sur d'autres contextes** — d'autres
domaines métier, d'autres types de problème (classification, régression),
d'autres datasets. C'est ce que cette galerie te propose.

Le but n'est pas de produire un beau livrable. C'est de **réexécuter le
pattern** vu en M1-B1 jusqu'à ce qu'il devienne automatique.

---

## Comment t'en servir

1. Ouvre la **fiche-pattern A4** (`ressources-publiques/fiche_pattern_ML_supervise.md`).
   Tu vas la mobiliser sur chaque notebook.
2. Choisis **un** notebook ci-dessous selon ton envie (ils sont par ordre croissant de difficulté).
3. (Optionnel) Si tu veux partager, mets 3 lignes sur Discord canal
   `#galerie-reentrainement` : dataset, métrique de référence, ce qui t'a
   surpris.

Pas de grille d'évaluation. Pas de note. Juste de la répétition.

---

## Les notebooks disponibles

| Notebook | Domaine métier | Type de problème | Autonomie | Temps estimé |
|---|---|---|---|---|
| [`01_classification_sante.ipynb`](01_classification_sante.ipynb) | Santé — mutuelle fictive Médicia+ | Classification binaire (tri biopsies) | 🟢 **Résolu** (tu lis / exécutes) | ~2 h |
| [`02_regression_immobilier.ipynb`](02_regression_immobilier.ipynb) | Immobilier — plateforme fictive ImmoVista | **Régression** (estimation prix médian) | 🟢 **Résolu** | ~2 h |
| [`03_regression_diabete_TODO.ipynb`](03_regression_diabete_TODO.ipynb) | Santé — Institut Valmont (recherche) | Régression (progression diabète) | 🟠 **À compléter** (`# TODO`, pas de solution) | ~1 h 30 |
| [`04_classification_vin_autonome.ipynb`](04_classification_vin_autonome.ipynb) | Œnologie — Laboratoire ŒnoData | Classification **multiclasse** (cépage) | 🔴 **Énoncé seul** (zéro étape, zéro `# TODO`) | ~1 h 30 |

> 💡 Les quatre notebooks mobilisent **le même pattern en 6 étapes** que
> M1-B1. Seuls changent le dataset, le domaine métier et la **famille de
> problème**. C'est exactement le test : *le pattern tient-il quand le
> contexte change ?*

### 4 marches d'autonomie (l'ordre compte)

1. **🟢 Lire/exécuter un cas résolu** (01 ou 02) — tu vois le pattern complet
   tourner sur un nouveau contexte.
2. **🟠 Compléter un cas à trous** (03, `# TODO`) — tu **reconstruis** le code
   toi-même, en t'appuyant sur 01/02 + la fiche A4 comme référence. **Pas de
   solution fournie** ; le guidage **décroît** au fil du notebook.
3. **🔴 Traiter un énoncé seul** (04) — juste une demande client, **aucune
   étape, aucun `# TODO`**. Tu déroules tout le pattern de tête. C'est le test :
   *« est-ce que je sais refaire, seul·e ? »*
4. **⚫ Refaire de zéro sur ton propre repo** — prends encore un autre dataset
   (cf. plus bas) et recommence sans aucun support.

> La difficulté **technique** ne monte presque pas (les datasets restent
> simples) — c'est le **niveau de guidage qui baisse**. Tu peux toujours
> rouvrir un notebook résolu : transpose, ne copie pas.
>
> 💡 Fil rouge des 4 cas : donne-toi **deux références** à chaque fois —
> un **plancher** (`Dummy`, le modèle bête : *mon modèle apprend-il quelque
> chose ?*) et un **modèle simple** (`Ridge` / `LogisticRegression` : *le
> modèle complexe est-il seulement justifié ?*). Deux questions de pro à ne
> pas confondre. Tu verras souvent que le modèle simple fait presque aussi
> bien — coût, maintenance, explicabilité en moins.

---

## Datasets

Les quatre notebooks utilisent des datasets **fournis directement par
scikit-learn** :

- `01_classification_sante.ipynb` : `sklearn.datasets.load_breast_cancer()` —
  embarqué dans la lib, **aucun téléchargement requis**.
- `02_regression_immobilier.ipynb` : `sklearn.datasets.fetch_california_housing()` —
  téléchargé une seule fois au premier appel (~1 Mo) puis mis en cache
  local par scikit-learn.
- `03_regression_diabete_TODO.ipynb` : `sklearn.datasets.load_diabetes()` —
  embarqué dans la lib, **aucun téléchargement requis**.
- `04_classification_vin_autonome.ipynb` : `sklearn.datasets.load_wine()` —
  embarqué, **aucun téléchargement** (classification multiclasse, 3 classes).

Pas de compte à créer, pas d'API externe, pas de CSV à manipuler.

---

## Tu veux aller plus loin ?

- Prends un autre dataset scikit-learn ou OpenML tabulaire de ton choix
  ([catalogue OpenML](https://www.openml.org/search?type=data)) et applique
  le pattern dessus.


*Galerie de réentraînement — étagère optionnelle post-M1-B1.*