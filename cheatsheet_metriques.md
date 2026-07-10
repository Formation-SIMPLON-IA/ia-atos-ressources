# Cheatsheet — métriques d'évaluation

> **Ressource transverse — à garder ouverte de M1 à M9.** Réf rapide, pas un cours :
> *quelle métrique pour quel problème, comment la lire, le piège à éviter*.
>
> Consolide ce qui est vu en M1 (classification déséquilibrée), M4 (régression) et M6
> (exploitation). Les métriques marquées 🎓 sont dans le périmètre du **questionnaire
> certif C4**. À mettre en regard de la [`grille_decision_C4.md`](./grille_decision_C4.md).

---

## 0. La question d'abord : quelle tâche → quelles métriques ?

```
   Mon modèle prédit quoi ?
        │
        ├── une CLASSE (catégorie)          → § 1 Classification
        │      ex : défaut/pas défaut, catégorie de ticket
        │
        ├── une VALEUR continue             → § 2 Régression
        │      ex : prix, durée, consommation
        │
        └── un ORDRE / une liste pertinente → § 3 Ranking / reco
               ex : « top 5 produits à recommander »
```

> 💡 **Règle d'or** : on choisit la métrique **avant** de modéliser, à partir du
> **coût métier de l'erreur** — pas après coup pour faire joli. Et on évalue
> **toujours sur le jeu de test**, jamais sur le train.

---

## 1. Classification

### La matrice de confusion (tout en découle)

|  | Prédit positif | Prédit négatif |
|---|---|---|
| **Réel positif** | VP (vrai positif) | FN (faux négatif) |
| **Réel négatif** | FP (faux positif) | VN (vrai négatif) |

### Les métriques

| Métrique | Formule | Ce qu'elle répond | Quand l'utiliser |
|---|---|---|---|
| **Accuracy** 🎓 | (VP+VN)/total | « % de prédictions correctes » | Classes **équilibrées** seulement |
| **Précision** 🎓 | VP/(VP+FP) | « quand je dis positif, ai-je raison ? » | Quand un **faux positif** coûte cher (spam, alerte) |
| **Rappel (recall)** 🎓 | VP/(VP+FN) | « est-ce que je retrouve tous les positifs ? » | Quand un **faux négatif** coûte cher (fraude, maladie, panne) |
| **F1-score** 🎓 | 2·(P·R)/(P+R) | compromis précision/rappel | Classes **déséquilibrées**, pas de préférence FP/FN |
| **F1-macro** 🎓 | moyenne des F1 par classe | perf moyenne **toutes classes égales** | Multi-classes déséquilibrées (chaque classe compte) |
| **ROC-AUC** 🎓 | aire sous courbe ROC | « le modèle sépare-t-il les classes ? » (tous seuils) | Comparer des modèles, indépendamment du seuil |
| **PR-AUC** | aire sous courbe précision-rappel | idem, **mieux adaptée** au fort déséquilibre | Positifs très rares (< 5 %) |

### Le piège n°1 : l'accuracy sur classes déséquilibrées 🎓

Si 95 % des cas sont « négatif », un modèle qui prédit **toujours négatif** a **95 %
d'accuracy**… et ne sert à rien. Sur du déséquilibré, regarde **F1, recall, PR-AUC** —
jamais l'accuracy seule.

### Le compromis précision ↔ rappel (le coût de l'erreur)

On ne maximise pas les deux à la fois : monter le **seuil de décision** augmente la
précision et baisse le rappel (et inversement).

```
   Coût d'un FAUX NÉGATIF élevé   →   privilégier le RAPPEL
   (rater une fraude, une panne, une maladie)

   Coût d'un FAUX POSITIF élevé   →   privilégier la PRÉCISION
   (bloquer un client honnête, fausse alerte coûteuse)
```

> 💡 Le **seuil** (par défaut 0.5) est un **curseur métier**, pas une vérité. On
> l'ajuste selon le coût des erreurs (cf. seuil de rejet M7, seuil de revue M8).

---

## 2. Régression

| Métrique | Ce qu'elle mesure | Comment la lire | Piège |
|---|---|---|---|
| **MAE** 🎓 | erreur absolue moyenne | « en moyenne je me trompe de X unités » | dans l'**unité métier** (€, min) → la plus parlante |
| **RMSE** 🎓 | racine de l'erreur quadratique | comme MAE mais **pénalise les grosses erreurs** | sensible aux outliers |
| **R² (coef. détermination)** 🎓 | part de variance expliquée (0→1) | « 1 = parfait, 0 = aussi nul que prédire la moyenne » | un R² élevé peut cacher une **fuite de données** |
| **MAPE** | erreur **en %** | « je me trompe de X % en moyenne » | explose si des valeurs réelles ≈ 0 |

**Comment choisir** : MAE pour parler au client (unité concrète), RMSE si les grosses
erreurs sont graves, R² pour situer vs une baseline. Donne-les **ensemble**, jamais R²
seul.

> 💡 **Mise en perspective business** : « RMSE = 42 » ne veut rien dire seul. *« On se
> trompe en moyenne de 42 minutes sur une durée de séjour moyenne de 5 jours »* — ça,
> le client le comprend. C'est le geste attendu en M4 et au notebook certif.

---

## 3. Ranking / recommandation (survol) 🎓

Pour un problème de **reco** (« les 5 produits que ce client aimerait »), les métriques
classif/régression ne conviennent pas. On regarde la **pertinence du haut de liste** :

- **Precision@k** : parmi les *k* éléments recommandés, combien sont pertinents.
- **Recall@k** : parmi les éléments pertinents, combien sont dans le top *k*.

> 💡 Le questionnaire C4 mentionne la reco / le filtrage collaboratif : retiens qu'on
> y évalue la **qualité du classement**, pas une classe ou une valeur exacte.

---

## 4. Le réflexe « deux questions » (mobilisé dans toute la galerie)

Une métrique seule ne dit pas si le modèle est **bon**. Donne-toi deux repères :

1. **Un plancher** — le `DummyClassifier` / `DummyRegressor` (prédit la classe
   majoritaire ou la moyenne). *Mon modèle apprend-il seulement quelque chose ?*
2. **Un modèle simple** — `LogisticRegression` / `Ridge`. *Mon modèle complexe
   est-il seulement justifié ?*

> 💡 Souvent le modèle simple fait **presque aussi bien** — coût, maintenance et
> explicabilité en moins. C'est le filtre **sobriété** du parcours.

---

## 5. Pièges transverses 🎓

| Piège | Conséquence | Réflexe |
|---|---|---|
| **Accuracy sur déséquilibré** | « 95 % » trompeur | F1 / recall / PR-AUC |
| **Évaluer sur le train** | scores gonflés, modèle qui généralise mal | toujours un **jeu de test** séparé |
| **Fuite de données** | R²/accuracy quasi parfaits, irréalistes | vérifier qu'aucune feature ne contient la cible |
| **Comparer sur des splits différents** | comparaison invalide | **même split + mêmes métriques** pour tous les modèles |
| **Optimiser une métrique hors contexte** | « +2 % de F1 » inutile au métier | relier la métrique au **coût de l'erreur** |
| **R² ou RMSE seul** | lecture incomplète | donner MAE + RMSE + R² ensemble |

---

## 6. Où chaque métrique apparaît dans le parcours

| Module | Métriques mobilisées |
|---|---|
| **M1** (scoring) | accuracy, précision, rappel, F1, F1-macro, ROC-AUC (classif déséquilibrée) |
| **M4** (benchmark régression) | MAE, RMSE, R² + mise en perspective business |
| **M5** (éval continue) | seuils sur F1-macro / recall — blocage de release |
| **M6** (exploitation) | suivi des métriques dans le temps, dégradation, calibration |
| **M7-M8** (audit/conception) | métriques + **coût de l'erreur** dans les arbitrages |

---

## 7. Pour aller plus loin

- **scikit-learn — Model evaluation** : https://scikit-learn.org/stable/modules/model_evaluation.html
- Fiche-pattern [`fiche_pattern_ML_supervise.md`](./fiche_pattern_ML_supervise.md) (où placer l'évaluation dans le pipeline)
- [`glossaire_IA.md`](./glossaire_IA.md) (définitions express)

---

## 8. À retenir

- **La tâche commande la métrique** : classe → §1, valeur → §2, classement → §3.
- **Choisir la métrique à partir du coût de l'erreur**, avant de modéliser.
- **Jamais l'accuracy seule** sur du déséquilibré ; **jamais R² seul** en régression.
- **Toujours un plancher (Dummy) + un modèle simple** comme repères.
- **Évaluer sur le test, même split pour tous** — sinon la comparaison ne vaut rien.
- Une métrique se **traduit en langage métier** pour le client.
