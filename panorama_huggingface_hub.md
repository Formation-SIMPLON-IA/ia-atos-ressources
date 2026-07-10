# Panorama HuggingFace — utiliser un modèle pré-entraîné

> **Ressource transverse — à mobiliser dès M4-B2, réutilisée en M7 et M8.**
>
> Ce document pose **la carte de l'écosystème « modèles sur étagère »**. Là où
> [`panorama_modeles_ML.md`](./panorama_modeles_ML.md) situe les *familles* de
> modèles, celui-ci répond à une autre question : **comment mobiliser un modèle
> que quelqu'un d'autre a déjà entraîné**, sans le réentraîner.
>
> C'est **votre métier d'intégrateur** : sur le Parcours 2, vous *réutilisez* des
> modèles existants bien plus souvent que vous n'en entraînez. Savoir lire le Hub,
> évaluer un modèle avant de l'adopter, et le faire **sobrement**, est un geste
> professionnel central.
>
> Lecture : ~30 min. Un exemple qui tourne en 2 min + une checklist d'adoption.

---

## 1. Pourquoi HuggingFace ?

**HuggingFace** est devenu le **GitHub des modèles d'IA** : un dépôt public où des
milliers de modèles pré-entraînés (texte, image, audio, multimodal) sont partagés,
documentés et utilisables en quelques lignes.

Pour un intégrateur, l'intérêt est double :
- **Gain de temps colossal** : pas besoin de collecter un dataset, de payer du
  GPU, d'entraîner pendant des heures. On télécharge un modèle qui *marche déjà*.
- **Standardisation** : la même API (`transformers`) sert pour de la classification
  de texte, de la reconnaissance d'image, de la transcription audio… On apprend un
  geste, on le rejoue partout.

**Quand l'éviter ?** Quand un modèle classique entraîné maison (une régression
logistique sur vos données) est *plus précis, plus explicable et moins cher* — ce
qui arrive souvent sur du tabulaire simple. HuggingFace n'est pas une fin en soi :
c'est une option à comparer aux autres (cf. la
[`grille_decision_C4.md`](./grille_decision_C4.md)).

---

## 2. La carte du Hub

Le Hub (`huggingface.co`) contient trois types d'objets :

| Objet | Ce que c'est | Exemple |
|---|---|---|
| **Models** | Modèles pré-entraînés, prêts à charger | `distilbert-base-uncased-finetuned-sst-2-english` (sentiment) |
| **Datasets** | Jeux de données partagés | `imdb`, `squad`, `mnist` |
| **Spaces** | Démos interactives (Gradio/Streamlit) | une démo de génération d'image |

Chaque modèle a une **page** qui contient :
- sa **model card** (la doc — section 4),
- sa **licence**,
- des **tags** (tâche, langue, framework),
- parfois un **widget** pour tester en ligne sans rien installer.

> 💡 **Réflexe** : avant de coder quoi que ce soit, ouvre la page du modèle et
> teste-le dans le **widget en ligne**. Si le résultat te déçoit déjà là, inutile
> de l'installer.

---

## 3. L'API `pipeline()` — ça tourne en 2 minutes

La fonction `pipeline()` de la librairie `transformers` masque toute la complexité :
tokenisation, chargement du modèle, post-traitement. On précise une **tâche**, et
HuggingFace choisit (ou on précise) un modèle adapté.

```python
# pip install "transformers>=4.40" torch
from transformers import pipeline

# Analyse de sentiment (un modèle léger par défaut)
clf = pipeline("sentiment-analysis")
print(clf("Le service client a été remarquable."))
# [{'label': 'POSITIVE', 'score': 0.9998}]

# Classification zero-shot : on définit nos propres classes, sans entraînement
zs = pipeline("zero-shot-classification")
print(zs("Mon prélèvement de mutuelle est erroné",
         candidate_labels=["paie", "mutuelle", "congés", "formation"]))
# 'mutuelle' arrive en tête
```

Trois lignes, et on a un classifieur fonctionnel. **C'est exactement le geste
intégrateur** : mobiliser une capacité existante pour un besoin métier.

> 💡 **Tâches `pipeline()` courantes** : `sentiment-analysis`, `text-classification`,
> `zero-shot-classification`, `ner` (entités nommées), `summarization`,
> `translation`, `image-classification`, `automatic-speech-recognition`,
> `feature-extraction` (embeddings).

---

## 4. Lire une model card — le réflexe pro

Une **model card** est la fiche d'identité d'un modèle (concept formalisé par
Mitchell et al., 2018, revu en M7). C'est **la première chose à lire**, avant
d'adopter. Cherchez-y :

- **La tâche** : pour quoi le modèle a-t-il été entraîné ? (un modèle de sentiment
  anglais ne marchera pas en français.)
- **Les données d'entraînement** : sur quoi ? (un modèle entraîné sur des tweets
  ne transfère pas forcément à des comptes-rendus médicaux.)
- **Les limites et biais** déclarés par les auteurs.
- **Les métriques** annoncées et le jeu d'évaluation.
- **La licence** (section 5).

Un modèle **sans model card sérieuse** est un drapeau rouge : vous ne savez pas ce
que vous déployez. En contexte régulé (santé, RH — cf. M7/M8), c'est rédhibitoire.

---

## 5. Licences — le piège qui coûte cher

Un modèle « gratuit à télécharger » n'est pas forcément « libre d'usage commercial ».
Vérifiez **toujours** la licence :

| Licence | Usage commercial | Remarque |
|---|---|---|
| **Apache-2.0 / MIT** | ✅ oui | Les plus permissives |
| **CC-BY** | ✅ oui, avec attribution | |
| **CC-BY-NC** | ❌ **non commercial** | Piège classique : OK en formation, pas chez un client |
| **Llama / Gemma (licences maison)** | ⚠️ sous conditions | Lire les clauses (seuils d'utilisateurs, usages interdits) |
| **gated** (accès sur demande) | variable | Il faut accepter des conditions + token HF |

> 💡 **Réflexe client** : avant de recommander un modèle à un client, la licence
> passe avant la performance. Un modèle 2 % plus précis mais `CC-BY-NC` est
> inutilisable en production commerciale.

---

## 6. Checklist « avant d'adopter un modèle HF »

Avant d'intégrer un modèle dans un projet, passez cette grille (à coller dans vos
notes de cadrage / conception) :

- [ ] **Tâche** : le modèle fait-il *exactement* ce dont j'ai besoin ?
- [ ] **Langue / domaine** : entraîné sur des données proches de mon cas ?
- [ ] **Model card** : présente, sérieuse, avec limites déclarées ?
- [ ] **Licence** : compatible avec l'usage (commercial ? régulé ?) ?
- [ ] **Taille** : tient sur ma machine / mon infra cible ? (un modèle 7B ≈ 14 Go en mémoire)
- [ ] **Fraîcheur** : dernière mise à jour, maintenu ou abandonné ?
- [ ] **Coût d'inférence** : latence par requête acceptable pour mon volume ?
- [ ] **Alternative plus sobre** : un modèle plus petit ferait-il aussi bien ? (section 7)

---

## 7. Le filtre sobriété (essentiel)

Un modèle pré-entraîné est **souvent** le choix sobre : pas de réentraînement, pas
de GPU, pas de dataset à collecter. **Mais deux pièges** :

1. **Le gros modèle réflexe.** On prend le plus gros « parce qu'il est meilleur ».
   Sur un cas simple, un **modèle distillé** (`distilbert`, ~66M paramètres) ou un
   **mini-modèle d'embeddings** (`all-MiniLM-L6-v2`, ~22M) fait souvent *aussi bien*
   pour une fraction du coût d'inférence et de mémoire.
2. **Le coût d'inférence récurrent.** Un modèle gratuit à télécharger peut coûter
   cher à *faire tourner* (latence, mémoire, énergie) — surtout multiplié par le
   volume de requêtes. cf. [`cheatsheet_sobriete_couts.md`] (à venir).

```
   Régression logistique maison   →  ~0 Mo, <1 ms, explicable
   distilbert (sentiment)         →  ~250 Mo, ~30 ms
   LLM 7B (zero-shot généraliste) →  ~14 Go, ~secondes, opaque
```

> 💡 **Règle de sobriété** : commencer par le **plus petit modèle qui résout le
> besoin**. Ne monter en taille que si un gain est *prouvé* sur vos données. Sur du
> tabulaire, un modèle classique maison bat souvent un gros modèle HF — et reste
> explicable, ce que le client régulé exige.

---

## 8. Où HuggingFace intervient dans le parcours

| Module | Usage | Modèles typiques |
|---|---|---|
| **M4-B2** (vision) | Transfer learning + zero-shot CLIP | `resnet`, `clip-vit-base-patch32` |
| **M7-B2** (conception) | Embeddings pour RAG, choix LLM/SLM | `sentence-transformers/all-MiniLM-L6-v2`, Mistral, Llama |
| **M8-B2** (conception) | Arbitrage SLM vs LLM, zero-shot vs fine-tune | SLM 1-3B vs LLM 7B+ |

Dans tous ces cas, le geste est le même : **lire la model card → vérifier la
licence → tester → comparer à une alternative plus sobre → décider**.

---

## 9. Pour aller plus loin

- **Documentation `transformers`** : https://huggingface.co/docs/transformers/index
- **Le Hub** : https://huggingface.co/models
- **Les tâches `pipeline()`** : https://huggingface.co/docs/transformers/main_classes/pipelines
- **sentence-transformers** (embeddings) : https://www.sbert.net/
- **Model Cards (Mitchell et al., 2018)** : https://arxiv.org/abs/1810.03993

---

## 10. À retenir

- HuggingFace = **le GitHub des modèles** ; votre métier d'intégrateur, c'est de
  les **réutiliser**, pas de tout réentraîner.
- `pipeline()` rend une capacité IA fonctionnelle **en 3 lignes**.
- **Avant d'adopter** : model card + licence + taille + alternative sobre. La
  licence passe avant la performance.
- **Sobriété** : le plus petit modèle qui résout le besoin. Un modèle classique
  maison bat souvent un gros modèle HF sur du tabulaire — et reste explicable.
- HuggingFace est une **option à comparer** (grille C4), pas un réflexe.
