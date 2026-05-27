# Grille de décision C4 — Choisir un modèle IA

> **Livrable pédagogique majeur du parcours ATOS.**
> Construit collectivement en restitution **M4-B1** (mercredi midi), puis
> enrichi à chaque module (M4-B2, M7-B1, M7-B2, M8-B1).
> Réutilisé pour le **notebook certif M9**.
>
> **Statut** : version initiale (à compléter en cours de promo selon les
> arbitrages collectifs).

---

## 🎯 À quoi sert cette grille ?

Face à un besoin métier nouveau, **quel modèle choisir** ? La grille te
donne une **première lecture** structurée selon 4 axes :

1. **Volume de données disponible** (du peu au beaucoup)
2. **Complexité du signal** (linéaire ↔ non-linéaire ↔ structurel)
3. **Contraintes métier** (explicabilité, latence, coût, sobriété)
4. **Maintenance attendue** (réentraînement fréquent ou non, MLOps requis)

**Important** : la grille n'est **pas un oracle**. C'est un **support
de raisonnement** : tu te poses chaque axe, tu **justifies** ton choix
dans ton notebook (M4, M7, M8, certif).

---

## 📊 La grille (version initiale, à enrichir)

### Axe 1 — Volume de données

| Volume | Familles candidates |
|---|---|
| **< 1 k échantillons** | Linéaire (LinearRegression / Ridge), Arbre simple, *Zero-shot foundation model* (CLIP / GPT-4) |
| **1 k - 100 k** | Random Forest, Gradient Boosting (HGB, XGBoost), Transfer learning |
| **> 100 k** | Boosting tuné, Réseau de neurones, Transfer learning, Foundation model fine-tuné |
| **> 1 M** | Deep learning (custom), Transformers, distillation possible |

### Axe 2 — Complexité du signal

| Complexité | Familles candidates |
|---|---|
| **Linéaire** (corrélation directe features ↔ cible) | Linéaire (Ridge, Lasso), arbre simple en challenge |
| **Non-linéaire faible** (interactions modérées) | Random Forest, Gradient Boosting |
| **Non-linéaire forte** (interactions complexes) | Boosting tuné, Réseau de neurones |
| **Structurel** (image, texte, séquence) | CNN, Transformer, Transfer, Foundation model |

### Axe 3 — Contraintes métier

#### Explicabilité

| Besoin | Familles privilégiées |
|---|---|
| **Décision réglementaire** (crédit, santé, RH) | Linéaire, Arbre simple (lisible) |
| **Confort utilisateur** (peut être complexe) | Random Forest + SHAP, Boosting + SHAP |
| **Boîte noire acceptable** | Réseau de neurones, Transfer learning, Foundation model |

#### Latence d'inférence

| Contrainte | Familles privilégiées |
|---|---|
| **< 10 ms** (temps réel critique) | Linéaire, Arbre simple, RF distillée |
| **10 ms - 100 ms** | RF, Boosting, CNN léger, Transfer fine-tuné |
| **100 ms - 1 s** | Tous (y compris LLM API rapides) |
| **> 1 s acceptable** | Foundation model (CLIP zero-shot, LLM via API) |

#### Coût

| Budget | Familles privilégiées |
|---|---|
| **Train < 1 € / Inférence quasi nulle** | Linéaire, RF, Boosting léger |
| **Train < 100 € / Inférence < 0.01 € req** | Boosting tuné, Transfer learning, CNN léger |
| **Train < 10 000 € / Inférence < 1 € / req** | Fine-tuning foundation model, ViT, BERT |
| **API par requête** | LLM via API (GPT, Claude, Mistral, Gemini) |

### Axe 4 — Maintenance attendue

| Fréquence réentraînement | Familles privilégiées |
|---|---|
| **Jamais** (modèle statique) | Linéaire, Foundation model zero-shot |
| **Trimestrielle** (drift modéré) | RF, Boosting (CI/CD M5 OK) |
| **Mensuelle** (drift fort) | Boosting + MLOps complet (M5+M6) |
| **Continu / online** | Réseau de neurones avec partial_fit, ou re-fine-tuning programmé |

---

## 🗺️ Cartographie des modèles par contexte

| Modèle | Volume idéal | Explicabilité | Latence | Train rapide |
|---|---|---|---|---|
| **LinearRegression / Ridge** | < 100 k | ✅✅✅ | < 1 ms | ✅✅✅ |
| **RandomForest** | 1 k - 1 M | ✅ (SHAP requis) | 1-10 ms | ✅✅ |
| **HistGradientBoosting** | 1 k - 1 M | ✅ (SHAP requis) | 1-5 ms | ✅✅✅ |
| **CNN from scratch** | > 10 k (images) | ❌ (sauf Grad-CAM) | 10-50 ms | 🟡 |
| **Transfer learning (ResNet, ViT)** | 100+ (images) | ❌ (sauf Grad-CAM) | 50-200 ms | ✅ |
| **Zero-shot CLIP** | 0 (no train) | ❌ | 80-200 ms | ✅✅✅ (no train) |
| **LLM via API** | 0 (no train) | ❌ | 500 ms - 5 s | ✅✅✅ (no train) |
| **Réseau profond custom** | > 1 M | ❌ | 50 ms - 1 s | ❌ |

---

## 💼 Cas types pédagogiques (issus du parcours)

### Cas M1 / M4-B1 (Bike Sharing — régression saisonnière, ~17 k lignes)

- **Volume** : 1 k - 100 k → axe 1 = boosting envisageable
- **Complexité** : non-linéaire faible (interactions saison × heure) → axe 2 = ensemble
- **Explicabilité** : moyenne (actuaire OK avec SHAP) → axe 3 = RF + SHAP
- **Latence** : pas critique → axe 3 OK pour tout
- **Maintenance** : trimestrielle (drift saisonnier modéré) → axe 4 OK
- **Verdict type** : **HistGradientBoostingRegressor** (rapide + précis) ou
  RandomForest si explicabilité prime

### Cas M4-B2 (PCB Defect — vision industrielle, ~2 k images)

- **Volume** : 1 k - 100 k images → transfer learning ou zero-shot
- **Complexité** : structurel (image) → CNN, ViT, CLIP
- **Explicabilité** : limitée acceptable (TechniMatic OK avec Grad-CAM)
- **Latence** : 100 ms acceptable (contrôle qualité offline) → tout OK
- **Maintenance** : si nouveaux défauts apparaissent, réentraîner → CI/CD M5
- **Verdict type** :
  - **Transfer learning (ResNet-18)** si **labels disponibles**
  - **Zero-shot CLIP** si **MVP rapide sans labels**

### Cas M7-B1 / B2 (MediVox — santé) — *à compléter en M7*

### Cas M8 (4 cas tirés) — *à compléter en M8*

---

## 🧠 Méthode d'utilisation

Pour chaque nouveau besoin métier :

1. **Place le cas sur les 4 axes** (volume / complexité / contraintes /
   maintenance)
2. **Identifie 2-3 familles candidates** qui cochent les axes critiques
3. **Benchmark sur même split + mêmes métriques** (règle d'or
   comparabilité issue de M1)
4. **Choisis** en justifiant chiffré (vs *« j'aime ce modèle »*)
5. **Documente** la décision dans ton notebook avec un renvoi à cette grille

---

## 🔁 Évolution de la grille

| Version | Date | Modifications | Auteur·rice |
|---|---|---|---|
| v1.0 | 2026-?? (semaine M4) | Construction initiale en restitution M4-B1 | Promo ATOS G1 |
| v1.1 | 2026-?? (semaine M4 fin) | Ajout cas vision PCB après M4-B2 | Promo ATOS G1 |
| v2.0 | 2026-?? (semaine M7) | Ajout familles foundation models / LLM / RAG | Promo ATOS G1 |
| v2.1 | 2026-?? (semaine M8) | Ajout cas par tirage | Promo ATOS G1 |
| v3.0 | À voir | Consolidation finale | — |

> 💡 **La grille n'est jamais terminée.** Chaque cas nouveau enrichit
> notre lecture. Cette version v1.0 est **construite collectivement en
> mercredi M4-B1** avec la promo — pas par la formatrice seule.

---

## 📚 Pour aller plus loin

- **scikit-learn — *Choosing the right estimator*** : <https://scikit-learn.org/stable/machine_learning_map.html>
  (carte officielle, à connaître mais plus restreinte que cette grille)
- **AWS — *ML Decision Tree*** : <https://aws.amazon.com/blogs/machine-learning/which-aws-machine-learning-service-to-use/>
  (centré cloud, pertinent en M5+)
- **HuggingFace — *Choosing the right model*** : <https://huggingface.co/docs/transformers/index>
  (centré transformers, pertinent en M4-B2 / M7)

---

*Grille pédagogique ATOS — co-construite avec la promo. Version v1.0
initiale par Marianne Arrué (formatrice), 2026-05-26. À enrichir à chaque
restitution.*
