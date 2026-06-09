# Canevas de rétro-cartographie — M2-B1

> **À remplir d'abord SANS regarder ton notebook.** L'objectif n'est pas d'avoir
> tout juste, c'est de voir ce qui est ancré et ce qui ne l'est pas. C'est ce
> qui est flou qui est intéressant — tu en parles vendredi en RDV individuel.
>
> Temps : 15 min seul·e (mémoire) → 15 min avec ton notebook (compléter) → 15 min en binôme (s'expliquer).

---

## Ton parcours sur M2-B1, en 6 étapes

| # | Étape | Ce que j'ai fait concrètement | Fonction / commande utilisée | Pourquoi cette étape ? | Ce sur quoi j'ai buté |
|---|---|---|---|---|---|
| 1 | **Découvrir le dataset German Credit** |  |  |  |  |
| 2 | **Auditer la qualité (manquants, types, doublons, outliers)** |  |  |  |  |
| 3 | **Auditer l'éthique (variables sensibles, proxies, déséquilibres)** |  |  |  |  |
| 4 | **Choisir et justifier les prétraitements** |  |  |  |  |
| 5 | **Industrialiser le `Pipeline` (imputation + encodage + normalisation)** |  |  |  |  |
| 6 | **Adapter le pipeline à une variable imprévue + synthèse `audit.md`** |  |  |  |  |

---

## Trois questions courtes

**1. Si on te redonnait demain un autre dataset à préparer (par exemple : des données RH pour un tri de candidatures), quelles étapes resteraient identiques ?**

> _Réponds en 2-3 lignes_

---

**2. Quelle est la décision que tu as prise dans le brief dont tu n'es pas sûr·e qu'elle était la bonne ?**
*(Ex : stratégie d'imputation d'une valeur manquante, encodage d'une variable catégorielle, classer une variable comme « sensible » ou non…)*

> _Réponds en 2-3 lignes_

---

**3. S'il y a une fonction ou un concept que tu as utilisé sans vraiment comprendre, c'est lequel ?**
*(on peut retravailler en RDV vendredi.)*

> _Un seul concept suffit_

---

## En binôme (15 min, échange croisé)

Vous vous montrez votre canevas et chacun pose ces 3 questions à l'autre :

1. *Si je te disais : remplace l'imputation par la médiane par un `KNNImputer` (ou le `OneHotEncoder` par un `OrdinalEncoder`), qu'est-ce qui change dans ton pipeline — et est-ce que c'est justifié ici ?*
2. *Tu as repéré une variable comme « sensible ». Comment tu sais qu'elle pose un risque éthique — et qu'est-ce qu'un « proxy » d'une variable sensible ?*
3. *Imagine qu'on déploie ce pipeline en prod et qu'il reçoit une catégorie jamais vue à l'entraînement. Qu'est-ce qui se passe ? (indice : `handle_unknown`)*

Notez en bas du canevas **un point que votre binôme vous a aidé à clarifier**.

> Mon binôme m'a aidé·e à comprendre : ___________________________

---