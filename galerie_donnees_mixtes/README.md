# Galerie données mixtes — tabulaire + texte, multi-classe

> Étagère asynchrone, **optionnelle**, à utiliser quand tu veux (dès la fin de M4).
> Ce n'est pas un brief, il n'y a pas de livrable obligatoire.

---

## À quoi ça sert

Jusqu'ici tu as entraîné des modèles sur du **tabulaire** (M1, M4) et manipulé
du **texte** (M2) — mais toujours séparément. Or beaucoup de cas réels
combinent les deux : un ticket d'incident (métadonnées + description), un
avis client (profil + commentaire), un dossier (champs structurés + notes
libres)… et peut-être ton cas d'usage certif.

Cette galerie ancre **quatre gestes** que tu n'as pas encore pratiqués
ensemble :

1. le **pipeline mixte** (`ColumnTransformer` num + cat + TF-IDF) ;
2. la classification **multi-classe déséquilibrée** évaluée proprement
   (CV stratifiée, F1-macro, matrice de confusion 3×3) ;
3. le réglage face à des **coûts d'erreur asymétriques** (poids de classes,
   seuils de décision) ;
4. les **scénarios de données** (texte seul / tabulaire seul / complet —
   même geste que l'analyse avec/sans variables sensibles du canvas §4.3).

---

## Comment t'en servir

1. Garde ouvertes les fiches indiquées en tête de chaque notebook
   (`fiche_pattern_ML_supervise.md`, `fiche_pattern_texte_NLP.md`,
   `fiche_desequilibre_classes.pdf`, `cheatsheet_metriques.md`…).
2. Suis l'ordre : les notebooks s'enchaînent (le 02 repart du pipeline du 01).
3. (Optionnel) Partage sur Discord canal `#galerie` : ce qui t'a surpris,
   en 3 lignes.

Pas de grille d'évaluation. Pas de note. Juste de la répétition.

---

## Les notebooks

| Notebook | Ce que tu pratiques | Autonomie | Temps estimé |
|---|---|---|---|
| [`01_pipeline_mixte_avis_clients.ipynb`](01_pipeline_mixte_avis_clients.ipynb) | Pipeline mixte tabulaire+texte, 3 classes, CV stratifiée, matrice 3×3, scénarios de données | 🟢 **Résolu** (tu lis / exécutes) | ~2 h |
| [`02_couts_asymetriques_avis_clients.ipynb`](02_couts_asymetriques_avis_clients.ipynb) | Matrice de coûts métier, poids de classes, seuil de décision multi-classe, zone grise → human-in-the-loop | 🟢 **Résolu** | ~1 h 30 |
| [`03_haute_cardinalite_TODO.ipynb`](03_haute_cardinalite_TODO.ipynb) | Haute cardinalité (1 206 modalités) : piège du OneHot naïf, frequency encoding à coder soi-même, `TargetEncoder` et sa CV interne, scénario sans texte | 🟠 **À compléter** (`# TODO`, pas de solution, guidage décroissant) | ~1 h 30 |
| [`04_benchmark_autonome.ipynb`](04_benchmark_autonome.ipynb) | Benchmark élargi (XGBoost / LightGBM vs logistique / RandomForest, perf **et** coûts), scénario avec/sans variable sensible + recommandation de minimisation RGPD | 🔴 **Énoncé seul** (zéro étape, zéro `# TODO`) | ~2 h |

> 💡 Fil rouge identique aux autres galeries : un **plancher** (`Dummy`) et un
> **modèle simple** (régression logistique) comme doubles références. Sur du
> TF-IDF haute dimension, tu verras que le modèle simple est dur à battre —
> coût, maintenance et explicabilité en moins (réflexe grille C4).

---

## Dataset

Les notebooks utilisent **Women's E-Commerce Clothing Reviews** : 23 486 avis
clients réels et anonymisés (licence **CC0**, domaine public), habillés ici
dans la fiction NovaThread. Colonnes tabulaires (âge, rayon, division…) +
texte libre (l'avis) + note 1-5 transformée en cible à 3 classes.

- **Téléchargement automatique** dans la première cellule de chaque notebook
  (miroir public GitHub, ~8 Mo, aucun compte requis).
- **Hors ligne ?** Dépose le CSV dans `data/clothing_reviews.csv` à côté des
  notebooks (source d'origine : Kaggle, « Women's E-Commerce Clothing
  Reviews »).
- Les avis sont **en anglais** : les gestes (TF-IDF, poids, seuils) sont
  identiques en français, seuls les *stop words* changent.

## Installation

```bash
pip install -r requirements.txt
```

Tout tourne sur CPU en quelques minutes. Compatible Google Colab (aucune
dépendance exotique).

- Le notebook **03** utilise `TargetEncoder` en multi-classe →
  **scikit-learn ≥ 1.4** requis.
- Le notebook **04** demande `xgboost` et `lightgbm` (préinstallés sur
  Colab). Sur **macOS**, installe d'abord le runtime OpenMP :
  `brew install libomp` — sinon `libxgboost.dylib could not be loaded`.

---

*Galerie données mixtes — étagère optionnelle post-M4.*