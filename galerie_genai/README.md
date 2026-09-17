# Galerie GenAI — RAG · agents · fine-tuning

> Étagère asynchrone, **optionnelle** — pas un brief, pas de livrable, pas de note.
>
> ⚠️ **À faire APRÈS ton cas d'usage certif.** Le sujet certif est du ML
> classique : un LLM/RAG n'y a pas sa place (relis la grille C4 et la
> feuille de route). Cette galerie prépare tes **futurs** projets — c'est ta
> boîte à outils GenAI d'intégrateur, pas un raccourci pour la certif.

---

## À quoi ça sert

Le parcours t'a fait **concevoir** des architectures LLM/RAG/agents (M7-M8)
et utiliser des modèles packagés (M0-B2, M4-B2). Cette galerie te fait
**construire** — en local, sobrement, avec le réflexe qui te distingue :
**évaluer avant d'empiler**.

## Les notebooks

| Notebook | Ce que tu pratiques | Autonomie | Temps |
|---|---|---|---|
| [`01_rag_fondations.ipynb`](01_rag_fondations.ipynb) | L'anatomie complète d'un RAG (chunking → embeddings → ChromaDB → génération citée) et surtout son **évaluation** (hit@k, citations, questions pièges, seuil d'abstention) | 🟢 **Résolu** | ~2 h 30 |
| [`02_rag_techniques_menu.ipynb`](02_rag_techniques_menu.ipynb) | Le menu de dépannage : symptôme → technique → **re-mesure** (normalisation/rewriting, HyDE, reranking, semantic chunking, fusion RRF 🟠, juge d'ancrage 🟠) + la grille de décision RAG. Deux techniques paient ici, deux ne paient pas — c'est le point. | 🟢 sections 1-4, 🟠 sections 5-6 (`# TODO`) | ~3 h |
| [`03_agents.ipynb`](03_agents.ipynb) | Un agent from scratch (boucle ReAct + outils typés + **5 garde-fous**), la **prompt injection démontrée puis bornée** (moindre privilège, validation humaine conçue), puis le même agent en LangGraph (🟠) ; encart MCP | 🟢 parties 1-3, 🟠 partie 4 (`# TODO`) | ~2 h 30 |
| [`04_finetuning_lora.ipynb`](04_finetuning_lora.ipynb) | LoRA de bout en bout **sur Colab (GPU T4)** : quand fine-tuner vs RAG vs prompt, mesure avant/après sur jeu de test, export GGUF → Ollama. Cas : apprendre une **règle métier** (l'urgence) qu'un modèle ne devine pas | 🟠 **GPU requis** | ~3 h |

**Références** : *RAG made simple* (Nir Diamant) — les notebooks citent ses
chapitres ; repo compagnon ouvert à tous :
[github.com/NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques).

## Choisis ton modèle selon ta machine

Tout tourne en **local via Ollama** — aucune clé API, aucune donnée qui sort
de ta machine. Configure via la variable d'environnement `OLLAMA_MODEL` (ou
la cellule de config de chaque notebook) :

| Ta machine | Modèle conseillé | Alternative |
|---|---|---|
| < 8 Go RAM | `llama3.2:1b` | `qwen2.5:0.5b` |
| 8-16 Go RAM (cas courant) | `qwen2.5:1.5b` | `llama3.2:3b` |
| ≥ 16 Go / Apple Silicon récent | `qwen2.5:7b` | `mistral:7b` |
| Ollama impossible | `MOCK_MODE=1` | — |

En **MOCK_MODE**, la génération est remplacée par un gabarit déterministe :
tu gardes les gestes de chunking, embeddings, recherche et leurs métriques —
mais **pas une évaluation représentative de génération, de citations ou d'ancrage**.
Seule la rédaction des réponses est simulée. Les notebooks basculent
automatiquement en MOCK si Ollama est injoignable.

Le notebook 04 est l'exception : le fine-tuning demande un GPU → **Google
Colab (T4 gratuit)**, tout est indiqué dedans.

## Contenu du dossier

- `corpus_fastia/` — 13 documents internes fictifs (RH, IT, projets) : le
  terrain de jeu des notebooks 01-02 ;
- `eval/questions_eval.json` — 15 questions à réponse connue + 3 questions
  pièges hors périmètre : le **jeu d'évaluation de référence** (il se
  complète, il ne se modifie pas en cours de comparaison).
- `finetuning_data/` — dataset du notebook 04 : `train.jsonl` (273 exemples
  tickets SAV → JSON, format chat), `test.jsonl` (60 tickets + sortie
  attendue), `instruction.txt` (consigne système partagée entraînement/éval),
  `build_dataset.py` (génération reproductible, `random_state=42`).

## Installation

```bash
pip install -r requirements.txt
# + Ollama : https://ollama.com puis `ollama pull <modèle choisi>`
```

Premier lancement : ~470 Mo téléchargés pour le modèle d'embeddings
multilingue (mis en cache ensuite). Compatible Google Colab (MOCK_MODE ou
Ollama distant non couvert — reste en local de préférence).

---

*Galerie GenAI — étagère optionnelle, après le cas d'usage certif.*
