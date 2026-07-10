# Panorama GenAI — LLM, SLM, RAG, agents

> **Ressource transverse — amorcée en M4-B2, centrale en M7 et M8.**
>
> Ce document est le **pendant GenAI** de
> [`panorama_modeles_ML.md`](./panorama_modeles_ML.md). Il **situe** les approches
> à base de grands modèles de langage — sans hype. Objectif : que face à un besoin
> client, vous sachiez **ce que chaque approche résout**, son coût, et surtout
> **quand elle est du sur-engineering**.
>
> Le parcours assume une position claire : la GenAI est un **outil parmi
> d'autres**, pas une réponse par défaut. Un agent multi-LLM pour une
> classification binaire perd des points. Ce panorama vous donne les critères pour
> trancher.
>
> Lecture : ~30 min. Un document de référence + un glossaire + un arbre de décision.

---

## 1. De quoi parle-t-on ?

La **GenAI** (IA générative) regroupe les modèles qui **génèrent** du contenu
(texte, image, code) plutôt que de prédire une classe ou une valeur. Au cœur : les
**grands modèles de langage** (LLM), entraînés sur d'énormes corpus de texte.

Quatre briques à ne pas confondre :

| Brique | Une phrase | Coût/complexité |
|---|---|---|
| **LLM** | Un gros modèle de langage généraliste (GPT-4, Mistral Large, Llama 70B) | Élevé |
| **SLM** | Un *petit* modèle de langage (1-3B paramètres), souvent suffisant et local | Modéré |
| **RAG** | Brancher un LLM sur **vos** documents pour qu'il réponde *ancré* dessus | Modéré à élevé |
| **Agents** | Des LLM qui **coopèrent et décident** d'étapes en chaîne | Élevé à très élevé |

> 💡 Plus on descend dans ce tableau, plus on ajoute de la **puissance** — mais
> aussi du **coût, de la latence, de l'opacité et de la surface d'erreur**. La
> sobriété, c'est de s'arrêter au niveau le plus bas qui résout le besoin.

---

## 2. LLM vs SLM — la taille n'est pas une vertu

Un **LLM** (7B à 400B+ paramètres) est polyvalent mais coûteux : mémoire, latence,
souvent une API payante par token, et des données qui partent chez un fournisseur.

Un **SLM** (Small Language Model, 1-3B paramètres) tient souvent **en local**, coûte
une fraction, et **suffit largement** pour des tâches ciblées (classification,
extraction, reformulation simple).

| Critère | SLM (1-3B) | LLM (7B+) |
|---|---|---|
| Mémoire | ~2-6 Go, CPU possible | ~14 Go+, GPU souvent requis |
| Coût | faible / local | élevé / API à l'usage |
| Confidentialité | local = données maîtrisées | API externe = données qui sortent |
| Polyvalence | tâche ciblée | généraliste |

> 💡 **Réflexe** : pour une tâche *spécifique* (trier des tickets, extraire des
> champs), un SLM fine-tuné — ou même un **classifieur classique** — bat souvent un
> LLM généraliste, pour 10× moins cher. Le LLM se justifie quand la tâche demande
> une *vraie* compréhension ouverte du langage.

---

## 3. RAG — donner ses documents à un LLM

Un LLM seul **hallucine** et ne connaît pas vos documents internes. Le **RAG**
(Retrieval-Augmented Generation) corrige ça : on **retrouve** les passages
pertinents dans *votre* corpus et on les **injecte** dans le prompt.

```
   Question  ─►  Retriever  ─►  passages pertinents
                    │                    │
              Vector store          + Question
              (embeddings)               │
                                         ▼
                                   Prompt  ─►  LLM  ─►  Réponse ancrée
                                                          │
                                              (rien trouvé → abstention)
```

**Quand le RAG est pertinent** : il existe un **corpus documentaire** à interroger
(base de procédures, comptes-rendus, FAQ) et le besoin est de **répondre** en
s'appuyant dessus.

**Quand le RAG est du sur-engineering** : le besoin est de **classer** ou de
**prédire** (pas de répondre), ou le « corpus » tient en 5 documents (un simple
prompt suffit), ou les données sont tabulaires.

> 💡 Un RAG sans **fallback** (abstention si rien de pertinent n'est trouvé) est
> dangereux : il pousse le LLM à inventer. cf. mini-cours M7-B2.

---

## 4. Agents — quand (et quand pas)

Une architecture **multi-agents** fait coopérer des LLM spécialisés qui **décident**
des étapes (valider → prédire → expliquer → superviser), via un orchestrateur
(LangGraph, par ex.).

**Atout réel** : pour un **workflow multi-étapes hétérogène** avec supervision
humaine native (un agent superviseur route vers un humain en cas de doute).

**Le piège** : des agents pour une **décision atomique** (« quelle catégorie ? »)
ajoutent orchestration, coût, latence cumulée, debug difficile et points de panne —
pour **zéro gain**. C'est le sur-engineering caractéristique du tropisme GenAI.

> 💡 **Test simple** : si le problème est *une seule prédiction*, ce n'est pas un
> cas d'agents. Si c'est une *chaîne de raisonnement* avec des étapes de nature
> différente, alors peut-être.

---

## 5. Fine-tuning vs zero-shot vs prompt

Trois façons de mobiliser un LLM/SLM, de la plus légère à la plus lourde :

| Approche | Principe | Quand |
|---|---|---|
| **Zero-shot** | On demande au modèle généraliste sans exemple | Démarrage à froid, pas de données labellisées |
| **Few-shot (prompt)** | On met quelques exemples dans le prompt | Tâche cadrable par l'exemple, peu de données |
| **Fine-tuning** | On réentraîne le modèle sur ses données | Tâche spécifique récurrente + dataset labellisé |

> 💡 **Règle** : si on a un **dataset labellisé**, un modèle **supervisé** (classique
> ou SLM fine-tuné) est généralement *plus précis* qu'un zero-shot généraliste — et
> moins cher à l'inférence. Le zero-shot brille surtout au *démarrage à froid*.

---

## 6. Arbre de décision « ai-je besoin de GenAI ? »

```
   Mon besoin est-il de GÉNÉRER du langage / comprendre du texte ouvert ?
        │                                   │
       NON                                 OUI
        │                                   │
   ML classique /                  Ai-je un corpus de documents à interroger ?
   vision / tabulaire                 │                    │
   (pas de GenAI)                    NON                  OUI
                                      │                    │
                            LLM/SLM simple          RAG (+ fallback)
                            (prompt/zero-shot)            │
                                                  Le workflow est-il
                                                  multi-étapes hétérogène
                                                  avec décisions en chaîne ?
                                                       │          │
                                                      NON        OUI
                                                       │          │
                                                  on s'arrête   Agents
                                                  là            (si justifié)
```

> 💡 La plupart des cas métier s'arrêtent **bien avant** les agents. Descendre d'un
> cran de complexité doit toujours être **justifié par un gain prouvé**.

---

## 7. Glossaire express

- **Token** : unité de texte (≈ ¾ d'un mot) ; les LLM facturent au token.
- **Embedding** : représentation vectorielle d'un texte ; deux textes proches de
  sens ont des vecteurs proches. Base du RAG.
- **Vector store** : base qui indexe des embeddings pour une recherche par
  similarité (ChromaDB, FAISS).
- **Prompt** : l'instruction + le contexte envoyés au modèle.
- **Hallucination** : le modèle affirme avec aplomb quelque chose de faux.
- **Fine-tuning** : réentraîner un modèle pré-entraîné sur ses propres données.
- **Zero-shot** : faire faire une tâche sans aucun exemple d'entraînement.
- **Foundation model** : gros modèle pré-entraîné généraliste, réutilisable pour
  plein de tâches (LLM, CLIP…).
- **Contexte (fenêtre de)** : quantité de texte que le modèle peut traiter d'un coup.

*(Ces termes alimentent aussi le [`glossaire_IA.md`](./glossaire_IA.md) transverse.)*

---

## 8. Le filtre sobriété (position du parcours)

La GenAI est séduisante et survendue. Le parcours impose un **garde-fou explicite** :

- On part **toujours** de la solution la plus simple (souvent : ML classique).
- On ne monte en GenAI que si le besoin l'exige (langage ouvert, génération) **et**
  qu'un gain est démontré.
- On **chiffre** le coût (cf. estimation des coûts LLM, M7-B2) : un LLM en API peut
  coûter un ordre de grandeur de plus qu'un modèle local, multiplié par le volume.
- On **justifie ce qu'on n'a pas mis** (« pas d'agents car prédiction unique »,
  « pas de RAG car pas de corpus à interroger »).

> 💡 En conception (M7-B2, M8-B2) et en certif, un choix GenAI **non justifié** ou
> **disproportionné** est pénalisé. La sobriété n'est pas une contrainte
> pédagogique : c'est la meilleure ingénierie, et la posture la plus défendable en
> audit (conformité, coût, explicabilité).

---

## 9. Pour aller plus loin

- **AI Act (implications selon l'architecture)** : https://artificialintelligenceact.eu/the-act/
- **LangGraph (orchestration d'agents)** : https://langchain-ai.github.io/langgraph/
- **ChromaDB (vector store)** : https://docs.trychroma.com/
- **sentence-transformers (embeddings)** : https://www.sbert.net/
- **HuggingFace** : voir [`panorama_huggingface_hub.md`](./panorama_huggingface_hub.md)

---

## 10. À retenir

- 4 briques distinctes : **LLM** (gros, généraliste), **SLM** (petit, souvent
  suffisant), **RAG** (LLM + vos documents), **agents** (LLM qui coopèrent).
- Plus on descend, plus on ajoute coût, latence, opacité — **s'arrêter au plus bas
  qui résout le besoin**.
- **Dataset labellisé** → un supervisé bat souvent le zero-shot.
- **Pas de génération de langage** dans le besoin → probablement **pas de GenAI**.
- La GenAI est une **option à comparer** (grille C4), avec **garde-fou sobriété
  explicite** — jamais un réflexe.
