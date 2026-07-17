# 🏖️ Cahier de vacances FastIA — été 2026

> Intersaison du 13 juillet au 30 août · reprise **mardi 1ᵉʳ septembre** (M5)
> Rien n'est noté. Rien n'est présenté à l'oral. Tout est à la carte.

## L'histoire

Chez FastIA, l'été est l'intersaison : les missions tournent au ralenti et
chaque consultant en profite pour **entretenir sa pratique** — c'est même une
demande explicite de Karim, qui attend de chacun un petit « plan d'entretien
des compétences » avec une trace de ce qui a été travaillé. C'est exactement
ce que font les ESN réelles pendant la morte-saison.

Traduction pour toi : tu sors de M0-M4 avec le pattern ML supervisé complet
(données → préparation → entraînement → évaluation → choix de modèle). M5-M8
en septembre **suppose ce pattern acquis** — on n'y reviendra pas, on
construira dessus (déploiement, monitoring, architecture). L'objectif du
cahier : arriver le 1ᵉʳ septembre capable de re-dérouler ce pattern **sans
relire tes notes**.

## Les règles du jeu

- **À la carte** : tu choisis ce que tu fais dans le menu ci-dessous. Aucun
  item n'est obligatoire.
- **Volume conseillé : 1 à 3 h par semaine, pas plus** — et au moins
  **2 semaines complètement OFF**. De vraies vacances font partie du
  programme.
- **Deux documents à déposer avant le lundi 31 août 18h** dans ton repo perso
  (celui du canvas), dossier `ete-2026/` :
  1. [`fiche_suivi_ete.md`](./fiche_suivi_ete.md) — ta fiche de suivi remplie
     (même si tu as peu coché : c'est une photo honnête, pas un bulletin) ;
  2. [`journal_ete.md`](./journal_ete.md) — ton journal de l'été (1 page max)
     avec **tes 3 questions pour la rentrée**.
- **Pas de correction pendant l'été.** Les notebooks des galeries ont leur
  filet intégré : le notebook résolu qui précède dans la galerie + des
  résultats chiffrés attendus (ou des cellules d'assertions) pour t'auto-vérifier.
  Questions → Discord, réponse au fil de l'eau, sans garantie de délai.
- **À prévoir côté matériel** : tout tourne sur CPU, mais les 2 notebooks de
  la galerie modèles pré-entraînés téléchargent ~1,2 Go de modèles
  HuggingFace au premier lancement — prévois une connexion correcte et
  l'espace disque avant de partir en zone blanche.

## Le menu

### 🟢 Entretien — ne pas rouiller (~1 h par item)

1. **Relire une fiche-pattern** et la re-dérouler de tête :
   [`fiche_pattern_ML_supervise.md`](../fiche_pattern_ML_supervise.md),
   [`fiche_pattern_texte_NLP.md`](../fiche_pattern_texte_NLP.md),
   [`fiche_pattern_vision.md`](../fiche_pattern_vision.md) ou
   [`fiche_pattern_anonymisation_PII.md`](../fiche_pattern_anonymisation_PII.md).
2. **Glossaire** : parcourir les termes 🎓 du
   [`glossaire_IA.md`](../glossaire_IA.md) (ce sont ceux du questionnaire
   C1/C2/C4) — pour chacun, peux-tu l'expliquer en 1 phrase à un collègue ?
3. **Cheatsheet métriques** ([`cheatsheet_metriques.md`](../cheatsheet_metriques.md)) :
   rejouer « quelle métrique pour quel problème » sur 3 cas vus en M1/M2/M4.
4. **Refaire un notebook de galerie déjà fait** (les 01/02 de n'importe quelle
   galerie), sans regarder ta version précédente.
5. **Relire tes compétences** dans
   [`00_competences_referentiels.md`](../00_competences_referentiels.md)
   (C1 → C5) : pour chaque niveau coché en M0-M4, saurais-tu citer *où* tu
   l'as pratiqué ?
6. **Lire la carte des frameworks**
   ([`fiche_frameworks_deep_learning.md`](../fiche_frameworks_deep_learning.md),
   ~20 min) : situer sklearn / PyTorch / Keras-TF / Hugging Face — tu as
   manipulé PyTorch et CLIP en M4-B2, cette fiche remet la carte sous les
   gestes. Termine par son « test ultime » pour vérifier que la carte est en
   place.

### 🎯 Consolidation — le cœur du cahier (~1 h 30 – 2 h par notebook)

Les notebooks `_TODO` (à compléter) puis `_autonome` (sans filet) des trois
galeries, dans l'ordre d'autonomie croissante :

1. [`galerie_reentrainement/03_regression_diabete_TODO.ipynb`](../galerie_reentrainement/03_regression_diabete_TODO.ipynb)
2. [`galerie_reentrainement/04_classification_vin_autonome.ipynb`](../galerie_reentrainement/04_classification_vin_autonome.ipynb)
3. [`galerie_modeles_pretraines/03_similarite_embeddings_TODO.ipynb`](../galerie_modeles_pretraines/03_similarite_embeddings_TODO.ipynb)
4. [`galerie_modeles_pretraines/04_NER_anonymisation_autonome.ipynb`](../galerie_modeles_pretraines/04_NER_anonymisation_autonome.ipynb)
5. [`galerie_donnees_mixtes/03_haute_cardinalite_TODO.ipynb`](../galerie_donnees_mixtes/03_haute_cardinalite_TODO.ipynb)
6. [`galerie_donnees_mixtes/04_benchmark_autonome.ipynb`](../galerie_donnees_mixtes/04_benchmark_autonome.ipynb)

Conseil : 1 galerie par quinzaine, la fiche-pattern correspondante ouverte à
côté. Si un notebook résiste, note **où** ça a bloqué dans ton journal — c'est
la matière première de la rentrée.

### ⭐ Ambitieux — la répétition générale (optionnel, pour les gourmands)

**Un mini cas d'usage perso de bout en bout** : choisis un dataset public qui
te parle (UCI, OpenML, Kaggle — évite ceux déjà vus en formation), et déroule
les phases faisables dès maintenant de la
[`feuille_route_cas_usage.md`](../feuille_route_cas_usage.md) dans une copie
du [`canvas-cas-usage-v2.ipynb`](../canvas-cas-usage-v2.ipynb). C'est
littéralement le format de la certification — le faire une fois « pour de
faux » cet été, c'est de l'avance prise sur M9.

**Une lecture-pont vers M5** :
[`fiche_notebook_a_prod.pdf`](../fiche_notebook_a_prod.pdf) — versionner,
packager, servir, monitorer. Juste la lire : c'est le programme de la rentrée.

### 🚫 Ce que le cahier ne demande PAS (et c'est volontaire)

- **Pas de nouvelle techno d'industrialisation** : Docker, MLflow, RAG,
  agents… attendront M5-M8, avec les briefs faits pour. (Les galeries
  introduisent quelques bibliothèques ML nouvelles — XGBoost/LightGBM,
  sentence-transformers — mais toujours avec le mode d'emploi dans le
  notebook : c'est du même geste sklearn, pas une techno à apprendre.)
- **Pas de veille imposée**, pas de MOOC, pas de certification externe.
- **Pas de relecture des briefs M0-M4** : le cahier travaille les gestes, pas
  les énoncés.

## Séquençage indicatif (à adapter librement)

- **Quinzaine 1** (mi/fin juillet) : 🟢 au choix + galerie réentraînement
- **Quinzaine 2** (début août) : OFF total, ou 🟢 léger
- **Quinzaine 3** (mi-août) : galerie modèles pré-entraînés
- **Dernière semaine** (24-30 août) : galerie données mixtes **ou** ⭐ selon
  ton rythme (pas les deux — le plafond 3 h/semaine tient aussi en août),
  remplir fiche + journal, déposer avant le **lundi 31 août 18h**

Le 27 août tu recevras l'avant-module M5 : tes 3 questions du journal seront
reprises à la réactivation collective du mardi 1ᵉʳ septembre.

Bon été ☀️