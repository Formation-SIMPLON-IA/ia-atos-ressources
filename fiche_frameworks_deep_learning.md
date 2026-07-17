# Frameworks de deep learning — la carte (sklearn · PyTorch · Keras/TensorFlow · Hugging Face)

> **Culture pure, aucun hands-on** — comme la cheatsheet cloud. Tu as déjà
> *utilisé* PyTorch et CLIP en M4-B2 sans t'arrêter sur « c'est quoi, ce
> framework ? ». Cette fiche te donne la carte : qui fait quoi, lesquels tu
> croiseras en mission, et quoi répondre en entretien.
> Durée de lecture : ~20 min · Mobilisation : dès M4-B2, utile M5-M8 et entretiens.

---

## 0. La question à laquelle cette fiche répond

« Vous connaissez TensorFlow ? Et PyTorch ? » — question d'entretien
classique. La bonne réponse d'un **intégrateur IA** n'est pas de réciter des
API, c'est de **situer** : quel outil pour quel étage du travail, et pourquoi,
dans 90 % des missions, tu n'écriras **jamais** une boucle d'entraînement
deep learning toi-même.

L'idée centrale, déjà croisée dans le panorama Hugging Face :

> **Entraîner un réseau de neurones from scratch est un métier (data
> scientist / ML researcher). Consommer, adapter et déployer des modèles,
> c'est le tien.** Les frameworks ci-dessous se rangent naturellement le long
> de cette frontière.

---

## 1. La carte en un coup d'œil

```
            ÉTAGE                     OUTIL                 TU L'AS VU EN
┌──────────────────────────┬──────────────────────────┬────────────────────┐
│ ML classique (tabulaire) │ scikit-learn (+XGBoost/  │ M1, M2, M3, M6     │
│  ← LE DÉFAUT DU PARCOURS │  LightGBM)               │ galeries           │
├──────────────────────────┼──────────────────────────┼────────────────────┤
│ Deep learning : écrire   │ PyTorch  ·  Keras/       │ M4-B2 (option CNN) │
│ et entraîner des réseaux │ TensorFlow  ·  (JAX)     │                    │
├──────────────────────────┼──────────────────────────┼────────────────────┤
│ Consommer des modèles    │ Hugging Face             │ M4-B2 (CLIP),      │
│ pré-entraînés            │ transformers ·           │ galerie            │
│  ← TON GESTE PRINCIPAL   │ sentence-transformers ·  │ pré-entraînés,     │
│                          │ torchvision              │ M7-M8              │
├──────────────────────────┼──────────────────────────┼────────────────────┤
│ Servir / échanger        │ FastAPI · ONNX Runtime · │ M1-B2 (ton API !), │
│ un modèle                │ TorchServe / TF Serving ·│ M5 (servir ≠       │
│                          │ Ollama (LLM)             │ entraîner)         │
└──────────────────────────┴──────────────────────────┴────────────────────┘
```

> **⚠️ Un framework n'est pas un modèle.** C'est LA confusion à évacuer
> d'entrée :
> - **PyTorch, TensorFlow** = les *moteurs* qui exécutent les calculs ;
> - **CLIP, BERT, Llama, ResNet** = des *modèles* (des poids entraînés) ;
> - **Hugging Face** = le *catalogue* + les outils pour utiliser ces modèles.
>
> Dire « on a utilisé CLIP via Hugging Face, qui tourne sur PyTorch » range
> chaque mot à sa place.

L'empilement, vu en couches (pourquoi Hugging Face n'est PAS un concurrent
de PyTorch) :

```
   Ton application métier   (FastAPI, script, batch…)
            │
            ▼
   Hugging Face transformers  ← tu travailles ICI
            │
            ▼
   PyTorch / TensorFlow       (calcul tensoriel)
            │
            ▼
   CUDA (ou équivalent)       (accès au calcul GPU — c'est PyTorch qui
            │                  lui parle, jamais toi)
            ▼
   GPU / CPU                  (matériel)
```

Trois lectures de cette carte :

1. **scikit-learn n'est pas un framework de deep learning** — et c'est très
   bien. Pour du tabulaire (l'immense majorité des cas d'entreprise), il
   reste l'outil de référence, avec XGBoost/LightGBM pour la performance.
2. **PyTorch et Keras/TensorFlow jouent dans la même case** : écrire des
   réseaux. Tu choisis rarement — la mission, l'équipe ou le modèle
   pré-entraîné a déjà choisi pour toi.
3. **Hugging Face n'est pas un concurrent de PyTorch** : c'est un étage
   au-dessus. `transformers` *utilise* PyTorch (ou autre) sous le capot pour
   te servir des modèles prêts à l'emploi.

### Trente secondes d'histoire (pourquoi TensorFlow est encore partout)

```
~2010-2015   scikit-learn s'impose sur le ML classique — il y est toujours
2015         TensorFlow (Google) devient LA référence industrielle du deep
2017-2019    PyTorch (Meta) conquiert la recherche : plus simple à déboguer
2018-2022    Hugging Face devient le standard des modèles pré-entraînés
Aujourd'hui  PyTorch + Hugging Face dominent les nouveaux projets (dont la
             GenAI) ; TensorFlow reste massivement présent dans l'existant
```

C'est pourquoi tu entendras « tout le monde est sur PyTorch » ET tu
trouveras du TensorFlow dans la moitié des SI : les deux sont vrais — l'un
parle du neuf, l'autre du parc installé.

---

## 2. Les acteurs, un par un

### scikit-learn — le socle ML classique

- **Ce que c'est** : la bibliothèque Python de référence pour le ML
  *non-deep* : régressions, forêts, SVM, pipelines, métriques, validation.
- **Forces** : API unifiée (`fit`/`predict`), CPU, léger, mature, immense
  écosystème. Tout ton parcours M1-M6 est construit dessus.
- **Limites** : pas de réseaux de neurones sérieux, pas de GPU, pas d'images
  ou de texte brut sans featurisation (TF-IDF, embeddings…).
- **En mission** : partout où les données sont tabulaires — scoring, churn,
  détection d'anomalies, prévision. **Commencer ailleurs doit se justifier.**

### PyTorch — le standard deep learning actuel

- **Ce que c'est** : framework de calcul tensoriel + réseaux de neurones,
  open source (Meta → Linux Foundation). Style impératif « du Python normal » :
  il donne un contrôle très fin — on *peut* écrire explicitement la boucle
  d'entraînement (c'est ce que montrait M4-B2), même si des surcouches
  existent pour l'éviter (PyTorch Lightning, HF Accelerate).
- **Forces** : dominant en recherche et dans les modèles récents (la
  quasi-totalité des modèles Hugging Face sont des poids PyTorch),
  écosystème riche (torchvision, torchaudio), débogage naturel.
- **Limites** : plus bas niveau que Keras — verbeux pour un cas simple ;
  l'entraînement sérieux demande GPU et savoir-faire (learning rate,
  overfitting… le métier du data scientist).
- **En mission** : tu le croises surtout **indirectement** — c'est le moteur
  sous les modèles que tu intègres. En M4-B2, l'option « CNN from scratch »
  t'a montré à quoi ressemble le code ; l'option transfer learning
  (torchvision + ResNet18) est le geste réaliste.

### Keras / TensorFlow — l'historique industriel

- **Ce que c'est** : TensorFlow (Google, 2015) a été la référence
  industrielle du deep de la fin des années 2010. **Keras** est son API haut niveau : déclarer un
  réseau en quelques lignes (`model.compile()`, `model.fit()`) sans écrire la
  boucle d'entraînement. Depuis Keras 3, l'API est **multi-backend** : le
  même code Keras peut tourner sur TensorFlow, PyTorch ou JAX. L'image qui
  aide : **Keras = une « API universelle » pour décrire un réseau ;
  TensorFlow ou PyTorch = les moteurs qui exécutent réellement les calculs.**
- **Forces** : API la plus simple pour apprendre et prototyper ; outillage de
  déploiement mature (TF Serving, LiteRT ex-TF Lite pour mobile/embarqué,
  TensorFlow.js pour le navigateur).
- **Limites** : perte de terrain net face à PyTorch pour les modèles récents ;
  beaucoup de projets TF en entreprise sont aujourd'hui du **legacy à
  maintenir** plutôt que du choix neuf.
- **En mission** : tu en hériteras (« on a un modèle TF de 2021 à maintenir /
  migrer »), tu le choisiras rarement pour du neuf — sauf embarqué/mobile où
  son outillage reste une référence.

### Hugging Face (`transformers`, `sentence-transformers`) — l'étage consommation

- **Ce que c'est** : pas un framework d'entraînement, mais la **couche
  d'accès aux modèles pré-entraînés** (relis le panorama Hugging Face) :
  `pipeline()` en 3 lignes, model cards, Hub.
- **En mission** : c'est **ton geste principal** sur l'image, le texte et les
  embeddings — celui des galeries et de M7-M8. Le réflexe : chercher un
  modèle pré-entraîné AVANT d'envisager d'entraîner quoi que ce soit.

### Les seconds rôles (à savoir nommer, pas à pratiquer)

Dans l'ordre du cycle de vie — entraîner (tabulaire, puis deep), exporter,
servir (général, puis LLM) :

- **XGBoost / LightGBM** : pas du deep — le gradient boosting, complément
  naturel de scikit-learn sur le tabulaire (vus dans la galerie données
  mixtes).
- **JAX** (Google) : framework de recherche haute performance ; tu n'en
  entendras parler que si le client fait de la recherche.
- **ONNX** : un **format d'échange et de déploiement** de modèles, pas un
  framework — exporter un modèle PyTorch en ONNX pour le servir dans un
  runtime optimisé (y compris depuis C#/Java). Très pertinent pour un profil
  intégrateur.
- **FastAPI** : oui, il a sa place sur cette carte — c'est **ton** outil de
  l'étage « servir » (M1-B2, M5) : un modèle sklearn ou PyTorch derrière une
  API maison. TorchServe / TF Serving / ONNX Runtime sont les versions
  industrialisées et spécialisées du même geste.
- **Ollama** : serveur local de LLM (vu en M2 bonus, revu M7-M8) — étage
  « servir », spécialisé modèles de langage.

---

## 3. Tableau comparatif

| Critère | scikit-learn | PyTorch | Keras / TensorFlow | HF transformers |
|---|---|---|---|---|
| **Étage** | ML classique | écrire du deep | écrire du deep (haut niveau) | consommer du deep |
| **Données cibles** | tabulaire | tout (image, texte, audio…) | tout | texte, image, audio pré-entraînés |
| **Niveau requis** | 🟢 acquis dans le parcours | 🔴 métier DS | 🟠 API simple, expertise réelle pour bien entraîner | 🟢 acquis dans le parcours |
| **GPU** | non | pour entraîner, oui | pour entraîner, oui | souvent inutile en inférence (modèles légers CPU) |
| **Tendance** | stable, incontournable | dominant sur le neuf | legacy industriel + embarqué | standard de facto |
| **Ton usage type** | entraîner un modèle tabulaire | lire/adapter du code existant | maintenir/migrer de l'existant | intégrer un modèle en 3 lignes |

---

## 4. L'arbre de décision (le même que toujours)

1. **Données tabulaires ?** → scikit-learn (+ XGBoost/LightGBM si besoin).
   Le deep learning sur du tabulaire est presque toujours du sur-engineering.
2. **Image / texte / audio ?** → chercher un **modèle pré-entraîné**
   (Hugging Face Hub, torchvision) : zero-shot d'abord, fine-tuning léger
   ensuite si nécessaire (le trio de M4-B2 : from scratch / transfer /
   zero-shot — et tu as vu pourquoi from scratch perd souvent).
3. **Entraîner un réseau from scratch ?** → cas rare : données très
   spécifiques, volume suffisant, budget GPU, et un data scientist dans
   l'équipe. Si un brief ou un client te le demande sans ces conditions,
   c'est ta grille C4 qui parle : **challenge la demande**.

---

## 5. Idées reçues et pièges d'entretien

| Idée reçue / piège | Réalité |
|---|---|
| « scikit-learn, c'est pour apprendre ; en vrai on utilise TensorFlow » | Inverse : sur du tabulaire d'entreprise, sklearn/XGBoost EST l'outil de prod. Le deep n'y apporte souvent rien. |
| « PyTorch vs TensorFlow, il faut choisir son camp » | Le choix est surtout dicté par l'existant et les modèles pré-entraînés disponibles. Et Keras 3 tourne sur les deux. |
| « Hugging Face est un framework concurrent de PyTorch » | Non : une couche au-dessus. Les poids que `pipeline()` charge sont (le plus souvent) du PyTorch. |
| « Keras = TensorFlow » | Historiquement lié, mais Keras 3 est multi-backend (TF, PyTorch, JAX). Dire « Keras, l'API haut niveau, aujourd'hui multi-backend » fait la différence en entretien. |
| « Il faut un GPU pour faire du deep » | Pour *entraîner* sérieusement, oui. Pour *inférer* avec des modèles légers (MiniLM, ResNet18, DistilBERT…), le CPU suffit — tout ton parcours le prouve. |
| « Plus le framework est récent/gros, mieux c'est » | Le réflexe sobriété s'applique aux frameworks comme aux modèles : l'outil le plus simple qui couvre le besoin. |
| « Plus de deep learning = meilleur modèle » | Sur des données tabulaires d'entreprise, un Random Forest ou XGBoost bat souvent un réseau profond — tu l'as mesuré toi-même dans la galerie données mixtes. |

**Symptôme → cause probable** (si tu mets les mains dans du code existant) :

| Symptôme | Cause probable |
|---|---|
| `model.fit(X, y)` en 1 ligne, pas de boucle | Keras (ou sklearn si pas de réseau) |
| Boucle `for epoch in range(...)` avec `loss.backward()` | PyTorch |
| Fichiers `.h5` ou dossier `saved_model/` | Monde TensorFlow/Keras |
| Fichiers `.pt` / `.pth` / `.safetensors` | Monde PyTorch / Hugging Face |
| Fichier `.onnx` | Modèle exporté pour un runtime de serving |
| `from transformers import pipeline` | Consommation Hugging Face — ton terrain |

---

## 6. Ce que tu peux dire en entretien (synthèse en 4 phrases)

> « Sur du tabulaire je travaille en scikit-learn, éventuellement XGBoost.
> Sur l'image ou le texte, mon premier réflexe est un modèle pré-entraîné —
> Hugging Face ou torchvision — en zero-shot ou transfer learning, plutôt que
> d'entraîner from scratch. Je suis capable de lire et d'adapter du code
> PyTorch existant — le standard actuel des
> modèles récents — et je sais situer Keras/TensorFlow, que je croiserais
> surtout sur de l'existant à maintenir ou de l'embarqué. Et pour le serving,
> je sais qu'un modèle s'exporte et se sert indépendamment de son framework
> d'entraînement — ONNX, TorchServe, ou une API FastAPI comme on l'a fait. »

## 7. Le test ultime

Cette fiche a rempli son rôle si tu sais **placer un nom que tu n'as jamais
étudié**. Essaie : à quel étage de la carte vivent `vLLM`, `TensorRT`,
`OpenVINO`, `MLX` ?

<details>
<summary>👉 Réponses</summary>

- **vLLM** : étage « servir », spécialisé LLM (comme Ollama, version haute
  performance pour la prod GPU).
- **TensorRT** (NVIDIA) et **OpenVINO** (Intel) : étage « servir » —
  runtimes d'inférence optimisés pour leur matériel (souvent alimentés via
  un export ONNX).
- **MLX** (Apple) : étage « écrire du deep », comme PyTorch, optimisé pour
  les puces Apple Silicon.

Si tu as su raisonner « moteur ? modèle ? catalogue ? serving ? » sans
connaître ces outils, la carte est en place.

</details>

## 8. Pour aller plus loin

- **Le compagnon pratique de cette fiche** :
  `notebook_lire_code_deep.ipynb` — le même modèle écrit en Keras puis
  PyTorch (sorties déjà exécutées, rien à installer), pour voir en vrai tout
  ce que cette carte décrit.
- Doc scikit-learn — [scikit-learn.org](https://scikit-learn.org) (« Choosing the right estimator »)
- Doc PyTorch — [pytorch.org/tutorials](https://pytorch.org/tutorials) (le « 60 Minute Blitz » pour lire du code)
- Keras 3 multi-backend — [keras.io](https://keras.io)
- Panorama Hugging Face du parcours — `panorama_huggingface_hub.md` (le geste détaillé)
- Fiche-pattern vision du parcours — `fiche_pattern_vision.md` (transfer learning appliqué)
- Géron, *Deep Learning avec Keras et TensorFlow* (3ᵉ éd.) — pour qui veut ouvrir le capot
