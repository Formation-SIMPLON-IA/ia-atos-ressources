# Fiche-pattern — Entraîner un modèle ML supervisé (classification)

> Format A4 recto-verso. À garder sous le coude de M1 jusqu'à M6.
> Le geste est le même quel que soit le dataset ou le modèle — seuls les détails changent.

---

## Recto — La séquence en 6 étapes

```
   [1] Charger              [2] Explorer (mini)        [3] Découper
   ─────────────            ───────────────────        ─────────────
   pd.read_csv              .shape / .head /           train_test_split
   schéma + types           .isna().sum()              stratify=y
                            .value_counts(y)           random_state=42
        │                         │                          │
        └─────────────────────────┴──────────────────────────┘
                                  ▼
   [4] Entraîner            [5] Évaluer                [6] Persister
   ─────────────            ─────────────              ─────────────
   model.fit(X_train,       model.predict(X_test)      joblib.dump(
              y_train)      f1_score / roc_auc           model, path,
                            confusion_matrix             compress=3)
                            classification_report
```

| # | Étape | Geste | Fonction clé | Piège typique |
|---|---|---|---|---|
| 1 | **Charger** | Lire le CSV, regarder ce qu'on a | `pd.read_csv()` | Mauvais séparateur, types mal inférés (`object` au lieu de `float`) |
| 2 | **Explorer** | Taille, manquants, équilibre des classes | `.shape`, `.isna().sum()`, `.value_counts()` | Y passer 2h — 15 min suffisent en N1 |
| 3 | **Découper** | Train/test reproductible et stratifié | `train_test_split(stratify=y, random_state=42)` | Oublier `stratify=y` → classes déséquilibrées dans le test |
| 4 | **Entraîner** | `fit` sur train uniquement | `model.fit(X_train, y_train)` | Fitter sur tout `X` (data leakage) |
| 5 | **Évaluer** | Métriques sur test (jamais sur train pour décider) | `f1_score`, `roc_auc_score`, `confusion_matrix` | Lire `accuracy` quand les classes sont déséquilibrées |
| 6 | **Persister** | Sauver le pipeline complet, pas le modèle seul | `joblib.dump(pipeline, path, compress=3)` | Sauver `clf` sans le preprocessing → impossible de prédire en prod |

---

### Les 3 invariants à mémoriser

1. **`random_state=42` partout** : pour que tu puisses reproduire le même résultat demain.
2. **Le test ne sert qu'à évaluer, jamais à décider d'un hyperparamètre.** Si tu changes le modèle après avoir vu le score test, recommence avec un nouveau split.
3. **On sauve le pipeline (preprocessing + modèle), pas le modèle seul.** Sinon les transformations ne sont pas appliquées au moment de la prédiction.

---

## Verso — Le squelette minimal qui marche

```python
from pathlib import Path
import pandas as pd
from sklearn.datasets import load_breast_cancer  # ou ton CSV
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, roc_auc_score, classification_report
import joblib

# [1] Charger
data = load_breast_cancer(as_frame=True)
X, y = data.data, data.target

# [2] Explorer (mini)
print(X.shape, y.value_counts().to_dict())

# [3] Découper
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# [4] Entraîner (pipeline = preprocessing + modèle)
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", RandomForestClassifier(n_estimators=200, random_state=42)),
])
pipeline.fit(X_train, y_train)

# [5] Évaluer
y_pred = pipeline.predict(X_test)
y_proba = pipeline.predict_proba(X_test)[:, 1]
print(f"F1 macro : {f1_score(y_test, y_pred, average='macro'):.3f}")
print(f"ROC-AUC  : {roc_auc_score(y_test, y_proba):.3f}")
print(classification_report(y_test, y_pred))

# [6] Persister
Path("models").mkdir(exist_ok=True)
joblib.dump(pipeline, "models/model_v1.joblib", compress=3)
```

---

### Comment l'adapter

| Tu veux changer… | Tu modifies… |
|---|---|
| Le dataset | L'étape [1] — `pd.read_csv("mon_fichier.csv")` puis `X = df.drop(columns="cible"); y = df["cible"]` |
| Le modèle | L'étape [4] — remplace `RandomForestClassifier(...)` par `GradientBoostingClassifier(...)`, `LogisticRegression(...)`, etc. La suite ne bouge pas. |
| Les hyperparamètres | L'étape [4] — change les arguments du modèle : `n_estimators`, `max_depth`, `class_weight`, etc. |
| Les métriques | L'étape [5] — `precision_score`, `recall_score`, `roc_curve`, etc. selon le besoin métier |

---

### Quand ça ne marche pas — diagnostic rapide

| Symptôme | Cause probable | Vérifier |
|---|---|---|
| `ValueError: could not convert string to float` | Colonnes catégorielles non encodées | `X.dtypes` — ajouter un `OneHotEncoder` dans le pipeline |
| Score test très différent du score train | Overfitting ou data leakage | A-t-on fitté un scaler sur tout `X` avant le split ? |
| `roc_auc_score` plante | Tu passes `y_pred` au lieu de `y_proba` | ROC-AUC attend des probabilités, pas des classes |
| `f1_score` très bas alors que `accuracy` élevé | Classes déséquilibrées | Toujours regarder F1 macro et la matrice de confusion |
| Le `.joblib` rechargé prédit n'importe quoi | Tu as sauvé le modèle sans le preprocessing | Sauve le `pipeline` complet, pas juste `pipeline["clf"]` |

---

*Fiche-pattern transverse — utilisable de M1 à M6. Pour la classification multi-classes, le pattern est identique : seules les métriques changent.*