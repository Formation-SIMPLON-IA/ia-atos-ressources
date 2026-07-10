# Galerie modèles pré-entraînés — pour ancrer le geste d'intégration

> Étagère asynchrone, **optionnelle**, à utiliser quand tu veux.
> Ce n'est pas un brief, il n'y a pas de livrable obligatoire.

---

## À quoi ça sert

La [`galerie_reentrainement/`](../galerie_reentrainement/) ancre le geste
**« entraîner un modèle »** (C5). Celle-ci ancre l'autre moitié de ton métier
d'intégrateur : **« utiliser un modèle que quelqu'un d'autre a déjà entraîné »**.

Sur le Parcours 2 (professionnels IT), tu **réutilises** des modèles existants au
moins aussi souvent que tu n'en entraînes. Cette galerie te fait rejouer le geste
sur 4 contextes (sentiment, tri zero-shot, similarité, anonymisation) jusqu'à ce
qu'il devienne automatique.

À lire d'abord : [`panorama_huggingface_hub.md`](../panorama_huggingface_hub.md)
(le Hub, les model cards, la checklist d'adoption, le filtre sobriété).

---

## Le pattern en 4 temps (commun aux 4 notebooks)

1. **Choisir** le modèle — model card, tâche, langue, licence, taille.
2. **Charger** via `pipeline()` (ou `sentence-transformers`).
3. **Tester + mesurer** — latence, taille du modèle.
4. **Comparer** à une alternative plus sobre → décider.

> 💡 **Fil rouge sobriété** (l'équivalent du « deux références » de la galerie de
> réentraînement) : à chaque cas, mesure le **coût** (taille + latence) et demande-toi
> *« un modèle plus petit, ou un classique maison, ferait-il aussi bien ? »*. Un modèle
> pré-entraîné est souvent le choix sobre (zéro entraînement) — **mais** un gros modèle
> a un coût d'inférence récurrent. Le plus puissant n'est presque jamais la bonne
> réponse ; le plus **simple qui résout le besoin**, si.

---

## Les notebooks disponibles

| Notebook | Geste | Tâche | Autonomie | Temps |
|---|---|---|---|---|
| [`01_sentiment_avis_clients.ipynb`](01_sentiment_avis_clients.ipynb) | `pipeline()` | Sentiment d'avis (FluxPay) | 🟢 **Résolu** | ~1 h |
| [`02_zero_shot_tickets.ipynb`](02_zero_shot_tickets.ipynb) | zero-shot | Tri de tickets sans labels (CapGroup) | 🟢 **Résolu** | ~1 h |
| [`03_similarite_embeddings_TODO.ipynb`](03_similarite_embeddings_TODO.ipynb) | embeddings + cosinus | Détecter les doublons (support FAQ) | 🟠 **À compléter** (`# TODO`) | ~1 h 30 |
| [`04_NER_anonymisation_autonome.ipynb`](04_NER_anonymisation_autonome.ipynb) | NER | Pseudonymiser des logs (Acerox) | 🔴 **Énoncé seul** | ~1 h 30 |

### 4 marches d'autonomie (l'ordre compte)

1. **🟢 Lire/exécuter** (01, 02) — tu vois le pattern complet tourner.
2. **🟠 Compléter** (03, `# TODO`, pas de solution) — tu reconstruis le code, guidage décroissant.
3. **🔴 Énoncé seul** (04) — juste une demande client, aucune étape. *« Sais-je refaire, seul·e ? »*
4. **⚫ De zéro** — reprends une autre tâche HuggingFace (résumé, traduction, transcription audio…) sans support.

> La difficulté technique ne monte presque pas — c'est le **guidage qui baisse**.
> Tu peux toujours rouvrir un notebook résolu : transpose, ne copie pas.

---

## Modèles utilisés (légers, CPU, français)

| Notebook | Modèle | Taille | Dépendances notables |
|---|---|---|---|
| 01 | `nlptown/bert-base-multilingual-uncased-sentiment` | ~670 Mo | — |
| 02 | `MoritzLaurer/mDeBERTa-v3-base-mnli-xnli` | ~560 Mo | **`sentencepiece` + `protobuf`** (cf. piège) |
| 03 | `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | ~470 Mo | `sentence-transformers` |
| 04 | `Babelscape/wikineural-multilingual-ner` | ~700 Mo | — |

> ⚠️ **Premier lancement = téléchargement du modèle** (connexion requise une fois,
> puis cache local dans `~/.cache/huggingface`). Tout tourne sur **CPU**.
>
> ⚠️ **Piège réel (notebook 02)** : le tokenizer multilingue zero-shot s'appuie sur
> *SentencePiece*. Erreur `SentencePiece library ... not found` ou `protobuf ... not
> found` → `pip install sentencepiece protobuf`.

---

## Installation

```bash
pip install -r requirements.txt
# ou, minimal :
pip install "transformers>=4.40" torch sentence-transformers scikit-learn pandas sentencepiece protobuf
```

Pas de compte HuggingFace requis (modèles publics, licences MIT/permissives).

---

## Tu veux aller plus loin ?

- Explore d'autres tâches `pipeline()` : `summarization`, `translation`,
  `automatic-speech-recognition` ([catalogue HuggingFace](https://huggingface.co/models)).
- Sur chaque nouvelle tâche, rejoue le **pattern en 4 temps** + le **filtre sobriété**.

---

*Galerie modèles pré-entraînés — étagère optionnelle, mobilisable dès M4-B2,
réutile en M7-M8. Pendant « intégration » de la
[`galerie_reentrainement/`](../galerie_reentrainement/).*
