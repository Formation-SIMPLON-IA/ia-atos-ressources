# Cheatsheet — sobriété & coûts

> **Ressource transverse — le garde-fou central du parcours.** Réf rapide :
> *comment chiffrer le coût d'une solution IA, et comment arbitrer sobre vs
> impressionnant*.
>
> Consolide ce qui est mobilisé en M4-B2 (comparaison économique vision), M7-B1
> (mesure psutil d'un système hérité), M7-B2 (estimation des coûts LLM) et M8
> (sobriété « ce qu'on n'a pas mis »). À mettre en regard de la
> [`grille_decision_C4.md`](./grille_decision_C4.md) et des panoramas
> [HuggingFace](./panorama_huggingface_hub.md) / [GenAI](./panorama_genai_llm_rag_agents.md).

---

## 0. La règle

> **Recommander la solution la plus simple/légère qui résout le besoin — pas la
> plus impressionnante.** Ne monter en complexité (DL → LLM → RAG → agents) que si
> un **gain est prouvé** et **chiffré**.

Recommander un LLM ou des agents « parce que c'est moderne » est pénalisé en
conception (M7-B2, M8-B2) **et** en certif. La sobriété n'est pas une contrainte
pédagogique : c'est la meilleure ingénierie (coût, maintenance, explicabilité) et la
posture la plus défendable en audit (conformité, AI Act).

---

## 1. Mesurer, pas estimer au doigt mouillé (`psutil`)

« Ça consomme beaucoup » ne vaut rien. On **chiffre** : temps, mémoire, taille.

```python
import os, time, psutil, joblib
from pathlib import Path

proc = psutil.Process(os.getpid())
rss0 = proc.memory_info().rss / 1e6                       # mémoire avant (Mo)
model = joblib.load("model.joblib")
t0 = time.perf_counter(); model.predict(X); lat = (time.perf_counter()-t0)*1000
print(f"RSS={proc.memory_info().rss/1e6:.0f} Mo | "
      f"inférence={lat:.1f} ms | "
      f"modèle={Path('model.joblib').stat().st_size/1e6:.1f} Mo")
```

| Mesure | Comment | À quoi ça sert |
|---|---|---|
| **Temps d'entraînement** | `time.perf_counter()` autour du `fit` | coût de (ré)entraînement |
| **Temps d'inférence** | autour du `predict`, à plusieurs volumes | coût récurrent, contrainte de latence |
| **Mémoire (RSS)** | `psutil.Process().memory_info().rss` | tient-il sur l'infra cible ? |
| **Taille du modèle** | `Path(...).stat().st_size` | stockage, transfert, démarrage |

> 💡 Mesurer **et comparer** à ≥ 1 alternative (cf. § 4). Une mesure sans point de
> comparaison ne permet aucun arbitrage.

---

## 2. Estimer un coût LLM (ordres de grandeur)

Les LLM en API facturent **au token** (≈ ¾ d'un mot). **L'output coûte souvent plus
cher que l'input.**

```
coût/requête ≈ tokens_in × prix_in + tokens_out × prix_out
coût/mois    ≈ coût/requête × requêtes/jour × 30   (+ embeddings si RAG)
```

**Démarche** (toujours sur une **hypothèse de volume explicite**) :
1. Pose un volume : ex. *5 000 requêtes/jour*.
2. Estime tokens in/out par requête (ex. 500 in + 100 out).
3. Multiplie par les tarifs publics → **ordre de grandeur**, pas le centime.

> 💡 **Faux précis interdit** : « ~500 €/mois » est crédible ; « 487,32 €/mois » ne
> l'est pas. Et précise toujours l'hypothèse de volume — sans elle, deux estimations
> ne sont pas comparables.

**API vs self-host** : une API (OpenAI/Anthropic/Mistral) = pas d'infra mais coût
récurrent par appel + données qui sortent ; un modèle self-hosté = coût fixe
GPU/serveur mais données maîtrisées.

---

## 3. Les coûts cachés (souvent le vrai sujet)

Le coût **compute** est souvent faible ; ce qui pèse vraiment :

| Coût caché | Exemple |
|---|---|
| **Latence / UX** | un LLM à 2 s/requête dégrade l'expérience vs un modèle à 5 ms |
| **Maintenance** | une stack RAG/agents = plus de briques à maintenir et déboguer |
| **Dépendance fournisseur** | changement de tarif ou de modèle d'API subi |
| **Dette opérationnelle** | observabilité, montée de version, expertise rare |
| **Conformité** | données sensibles envoyées à une API externe (RGPD, AI Act) |
| **Énergie / empreinte** | un gros modèle consomme à chaque inférence (§ 5) |

> 💡 En audit (M7-B1), le constat récurrent : *le vrai coût d'un système bricolé
> n'est pas le compute, c'est la dette opérationnelle.*

---

## 4. Ordres de grandeur — repères mémoire

Pour un même cas simple (ex. classer du texte), du plus sobre au plus lourd :

| Approche | Mémoire | Latence | €/mois (indicatif) | Explicabilité |
|---|---|---|---|---|
| **Régression log. / arbre maison** | ~0 Mo | < 1 ms | ~50 (hébergement) | forte |
| **Modèle distillé** (`distilbert`, `MiniLM`) | ~100-300 Mo | ~10-30 ms | modeste | moyenne |
| **LLM 7B+ en API** (zero-shot) | n/a (distant) | ~0,5-2 s | ~300-800 | faible |
| **Multi-agents (LLM orchestrés)** | n/a | latence **cumulée** | ~200-500+ | faible |

> 💡 Ordre de grandeur **typique** : une API LLM coûte ~**10×** un modèle classique
> hébergé, pour un gain **non démontré** sur du tabulaire ou une classification
> simple. D'où la question rituelle : *le gain justifie-t-il le surcoût ?*

---

## 5. Énergie & empreinte — honnêteté, pas greenwashing

- Un modèle **plus petit** = moins de calcul = moins d'énergie, à chaque inférence,
  **multiplié par le volume**. C'est l'argument de sobriété le plus concret.
- **N'invente pas** un chiffre CO₂ précis : donne un **ordre de grandeur** ou parle
  en relatif (« ~10× moins de calcul »). Un faux chiffre est pire que pas de chiffre.
- La sobriété énergétique **rejoint** la sobriété économique : le plus léger est
  souvent à la fois le moins cher **et** le moins consommateur.

---

## 6. Arbitrer — sobre vs impressionnant

Grille de décision rapide :

```
   Une solution plus simple répond-elle au besoin ?
        │
       OUI  ───►  on la prend. (et on le dit : « pas besoin de X »)
        │
       NON  ───►  le gain de la solution complexe est-il PROUVÉ + CHIFFRÉ ?
                       │                 │
                      OUI               NON
                       │                 │
                 on monte d'un      on reste sobre
                 cran, justifié     (le « moderne » ne se justifie pas seul)
```

**Le geste « justifier ce qu'on n'a PAS mis »** (attendu en M8-B2) : un dossier de
conception sobre **explicite ses absences** —
> *« pas de vector DB car pas de corpus à interroger », « pas d'agent car prédiction
> unique », « pas de LLM car dataset labellisé → un supervisé est plus précis et 10×
> moins cher ».*

C'est ce qui distingue un choix **réfléchi** d'un réflexe.

---

## 7. Monitorer un LLM en production (ce qui change)

Le monitoring d'un modèle classique (cf.
[`cheatsheet_mlops_deploiement.md`](./cheatsheet_mlops_deploiement.md)) repose
sur trois hypothèses : latence en ms, coût marginal ~nul, métrique de qualité
calculable. Un LLM casse les trois :

| Ce qui change | Modèle ML classique | LLM en prod |
|---|---|---|
| **Latence** | stable, ~ms | variable et élevée (secondes), dépend de la longueur générée |
| **Coût / requête** | ~nul (infra fixe) | **non nul** (tokens in + out) — le coût devient une métrique à surveiller |
| **Qualité** | métrique calculable (F1, MAE) | non déterministe, pas de label → évaluation **par échantillonnage**, retours utilisateurs, ou LLM-as-a-judge (le geste vu en bonus M2-B2) |
| **Modes d'échec** | erreur HTTP, NaN | + refus de répondre, sortie au mauvais format (JSON cassé) |

Le mini-tableau de bord LLM :

| Métrique | Pourquoi |
|---|---|
| **Latence p95** | l'expérience des pires requêtes, pas la moyenne |
| **Coût / requête** (€) | la dérive budgétaire est silencieuse sans elle |
| **Tokens / requête** (in + out) | explique latence ET coût ; détecte les prompts qui gonflent |
| **Taux d'erreur de format** | sorties inexploitables par le code aval |
| **Score qualité échantillonné** | qualité mesurée sur un échantillon régulier, pas sur tout le trafic |

> 💡 Démonstration en **M5** (monitoring). Le réflexe : un LLM en prod se
> surveille comme un modèle classique **plus** un poste de coût et une qualité
> qu'on ne peut qu'échantillonner.

---

## 8. Où la sobriété est mobilisée dans le parcours

| Module | Geste de sobriété |
|---|---|
| **M4-B1/B2** | comparaison multi-critères (dont mémoire, vitesse) + comparaison économique des 3 approches vision |
| **M7-B1** | mesure psutil du système hérité + comparaison à une alternative légère |
| **M7-B2** | estimation des coûts LLM, recommandation avec garde-fou sobriété |
| **M8-B1/B2** | sobriété notée ; « justifier ce qu'on n'a pas mis » |
| **Galeries** | fil rouge « le plus simple qui résout » + deux références (Dummy + modèle simple) |

---

## 9. Pour aller plus loin

- **psutil** : https://psutil.readthedocs.io/en/latest/
- **Tarifs (ordres de grandeur)** : https://openai.com/api/pricing/ · https://mistral.ai/products/la-plateforme
- [`panorama_genai_llm_rag_agents.md`](./panorama_genai_llm_rag_agents.md) (filtre sobriété GenAI)
- [`cheatsheet_metriques.md`](./cheatsheet_metriques.md) (le réflexe « deux références »)

---

## 10. À retenir

- **Le plus simple qui résout le besoin** — monter en complexité seulement si le
  gain est **prouvé et chiffré**.
- **Mesurer** (psutil : temps, RSS, taille) **et comparer** — pas « ça consomme ».
- **Estimer un coût LLM** sur une **hypothèse de volume** explicite, en **ordres de
  grandeur** (input + output + embeddings).
- Le vrai coût est souvent **caché** : latence, maintenance, dépendance, conformité.
- Repère : une API LLM ≈ **10×** un modèle classique, pour un gain souvent non démontré.
- **Justifier ce qu'on n'a pas mis** = la marque d'un choix réfléchi.
