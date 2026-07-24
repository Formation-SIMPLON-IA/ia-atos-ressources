# Glossaire IA — vocabulaire du parcours

> **Ressource transverse vivante — à garder ouverte dès M0, enrichie à chaque module.**
>
> Public **IT non-data** : ce glossaire démystifie le vocabulaire de la data et de
> l'IA, terme par terme, en 1-2 lignes. Pas une encyclopédie — un repère rapide
> quand un mot revient dans un brief ou une question d'examen.
>
> Le tag `[Mx]` indique **où le terme apparaît pour la première fois** dans le
> parcours. Les termes utiles au **questionnaire certif** (C1/C2/C4) sont marqués 🎓.
>
> Ce fichier **grossit module après module** : si un terme te manque, signale-le,
> on l'ajoute. *(Couverture actuelle : M0 → M8.)*

---

## A

- **Abstention** `[M7]` — stratégie de repli où le système répond « je ne sais pas » plutôt que de forcer une réponse (utile en RAG quand aucun contexte pertinent n'est trouvé).
- **Accuracy (exactitude)** 🎓 `[M1]` — proportion de prédictions correctes. Trompeuse sur classes déséquilibrées (un modèle qui dit toujours « non » a 95 % d'accuracy si 95 % des cas sont « non »).
- **Agent (IA)** `[M7]` — un LLM doté d'outils qui décide d'étapes ; plusieurs agents peuvent coopérer (multi-agents). Souvent du sur-engineering hors workflow multi-étapes.
- **AI Act** 🎓 `[M2/M7]` — règlement européen encadrant les systèmes d'IA par niveau de risque (inacceptable / haut risque / limité / minimal).
- **Alembic** `[M3]` — outil de migration de schéma de base de données (versionner l'évolution des tables).
- **Anonymisation** `[M2/M7]` — rendre des données non ré-identifiables de façon **irréversible** (≠ pseudonymisation, réversible).
- **Arbitrage technique** `[M8]` — trancher un choix de conception (ML/DL, SLM/LLM, RAG, agents, zero-shot) avec un choix retenu + des raisons + une condition de changement d'avis.
- **Audit (IA)** `[M7]` — observer, documenter et hiérarchiser les risques d'un système existant (éthique / technique / ressources). On audite, on ne corrige pas.

## B

- **Baseline** 🎓 `[M1/M4]` — modèle de référence simple auquel on compare les autres. Deux planchers utiles : le `DummyClassifier` (plancher absolu) et un modèle simple bien réglé.
- **Biais (éthique)** 🎓 `[M2]` — traitement systématiquement défavorable d'un groupe ; se mesure (ex. disparate impact), se documente, parfois se corrige.
- **Biais / variance** `[M4]` — un modèle trop simple sous-apprend (biais élevé), trop complexe sur-apprend (variance élevée). Compromis à trouver.
- **Boucle de rétroaction (feedback loop)** `[M6]` — collecter les vrais labels a posteriori → réentraîner → promouvoir le modèle s'il est meilleur. Ferme le cycle MLOps.

## C

- **Cadrage** `[M8]` — définir le périmètre d'un projet (besoin réel reformulé, données existantes vs à acquérir, indicateurs, risques) **avant** toute conception.
- **Calibration** `[M6]` — un modèle est calibré si une probabilité de 0.8 correspond bien à 80 % de cas positifs. Peut se dégrader en production.
- **Chi² (test du)** `[M6]` — test statistique pour détecter le data drift sur variables **catégorielles** (vs KS pour les numériques).
- **CI/CD** `[M5]` — Intégration / Déploiement Continus : automatiser tests, build et livraison à chaque changement de code (GitHub Actions).
- **Classification** 🎓 `[M1]` — prédire une **classe** (catégorie). Binaire (2 classes) ou multi-classes.
- **ColumnTransformer** `[M2]` — outil scikit-learn pour appliquer des prétraitements différents à des colonnes différentes dans un pipeline.
- **Concept drift** `[M6]` — la **relation** entre features et cible change (ce qui prédisait un défaut hier ne le prédit plus). À distinguer du data drift.
- **Conteneur / Docker** `[M0/M5]` — empaqueter une application + ses dépendances pour qu'elle tourne pareil partout. `docker-compose` orchestre plusieurs conteneurs.
- **Contract test (modèle)** `[M5]` — test qui vérifie qu'un modèle respecte un contrat (mêmes colonnes en entrée, sortie déterministe) avant déploiement.
- **Contrat de données (data contract)** `[M3]` — spécification des colonnes, types et contraintes qu'un pipeline doit livrer en sortie ; le pipeline est conforme quand il **honore le contrat**, pas seulement quand il tourne.
- **Coût d'inférence** `[M7]` — coût (latence, mémoire, €) de **chaque prédiction** en production, multiplié par le volume. Souvent sous-estimé pour les LLM.

## D

- **Data drift** `[M6]` — la **distribution des données entrantes** change par rapport à l'entraînement (nouveaux profils clients). Mesuré par PSI, KS, Chi².
- **Dataset** 🎓 `[M1]` — jeu de données structuré (lignes = exemples, colonnes = features + cible).
- **Datasheet (Gebru)** `[M2]` — fiche documentant un dataset (origine, composition, biais, usages recommandés).
- **Déploiement** `[M5]` — mettre un modèle en service (conteneur, API) accessible et surveillé en production.
- **Disparate impact** 🎓 `[M2/M7]` — ratio de taux positif entre groupe défavorisé et favorisé. Règle des 4/5 : < 0.80 = signal de biais.
- **Distillation / modèle distillé** `[M7]` — version compressée d'un modèle (ex. `distilbert`), presque aussi performante pour une fraction du coût. Argument de sobriété.
- **Données semi-structurées** `[M3]` — données à structure souple sans schéma tabulaire strict (JSON, XML, logs) ; entre le structuré (table) et le non structuré (texte libre).
- **Drift (dérive)** `[M6]` — dégradation des performances d'un modèle en production, par data drift ou concept drift.

## E

- **EDA** 🎓 `[M2/M4]` — Exploratory Data Analysis : explorer les données (distributions, manquants, corrélations) avant de modéliser.
- **Embedding** `[M4/M7]` — représentation vectorielle d'un texte/image ; deux objets proches de sens ont des vecteurs proches. Base du RAG et de la recherche par similarité.
- **Epoch** `[M4]` — un passage complet sur tout le jeu d'entraînement (surtout en deep learning).
- **Évaluation continue** `[M5]` — re-mesurer les métriques du modèle sur un **jeu de référence** à chaque release ; **bloque la mise en prod** si dégradation au-delà d'un seuil.

## F

- **F1-score** 🎓 `[M1]` — moyenne harmonique précision/rappel ; métrique de choix sur classes déséquilibrées. F1-macro = moyenne non pondérée sur les classes.
- **Fallback (stratégie de repli)** `[M7]` — quoi faire quand le modèle n'est pas sûr : seuil de rejet, abstention, revue humaine (HITL). Choix de **conception**, distinct de la réaction au drift.
- **Feature** 🎓 `[M1]` — variable d'entrée du modèle (une colonne du dataset).
- **Feature engineering** `[M4]` — créer/transformer des features pour aider le modèle.
- **Fine-tuning** `[M4/M8]` — réentraîner un modèle pré-entraîné sur ses propres données.
- **Foundation model** `[M4]` — gros modèle pré-entraîné généraliste, réutilisable pour de nombreuses tâches (LLM, CLIP).
- **Fuite de données (data leakage)** 🎓 `[M4]` — une feature contient (directement ou indirectement) l'information de la cible → score artificiellement parfait, modèle inutile en vrai.

## G — H

- **GenAI** `[M7]` — IA générative : modèles qui génèrent du contenu (texte, image) plutôt que de prédire une classe/valeur.
- **GHCR / registry d'images** `[M5]` — registre où la CI/CD stocke les images Docker construites (GitHub Container Registry).
- **Grafana** `[M5]` — outil de **dashboards** pour visualiser les métriques de monitoring (alimenté par Prometheus). On construit son dashboard, on n'en importe pas un tout fait.
- **Hallucination** `[M7]` — un LLM affirme avec aplomb une information fausse ; le RAG et l'abstention la réduisent (sans la supprimer).
- **Haut risque (AI Act)** `[M7]` — catégorie de l'AI Act (Annexe III : santé, justice, emploi…) imposant transparence, traçabilité et supervision humaine.
- **Healthcheck** `[M5]` — endpoint (`/health`) indiquant si un service est vivant ; utilisé par docker-compose et le monitoring.
- **HITL (Human-in-the-loop)** `[M7]` — un humain valide ou tranche les cas incertains. Répond aux exigences de supervision de l'AI Act.
- **HuggingFace** `[M4]` — plateforme partageant des modèles pré-entraînés (« le GitHub des modèles »). cf. [`panorama_huggingface_hub.md`](./panorama_huggingface_hub.md).
- **Hyperparamètre** `[M1/M4]` — réglage choisi **avant** l'entraînement (nombre d'arbres, profondeur) ; ≠ paramètre, appris pendant.

## I — J — K

- **Idempotent** `[M3]` — une opération qu'on peut relancer sans effet de bord (ré-ingérer un fichier ne duplique pas les lignes).
- **Imputation** `[M2]` — remplacer les valeurs manquantes (par la moyenne, la médiane, la modalité la plus fréquente…).
- **Indicateur business (KPI)** 🎓 `[M8]` — mesure chiffrée du gain métier (temps gagné, € économisés) ; ≠ **métrique modèle** (F1, RMSE), qui en est le moyen.
- **Inférence** 🎓 `[M1]` — utiliser un modèle entraîné pour prédire (`model.predict`), par opposition à l'entraînement.
- **Jeu de référence** `[M5]` — échantillon stable servant à re-mesurer la performance du modèle release après release (évaluation continue).
- **KS (test de Kolmogorov-Smirnov)** `[M6]` — test statistique comparant deux distributions ; sert à détecter le data drift sur features numériques.

## L — M

- **Latence** `[M5]` — temps de réponse d'une prédiction (souvent mesurée en p50/p95). Contrainte clé en production et dans l'arbitrage de sobriété.
- **Lineage (traçabilité de la donnée)** `[M3]` — tracer l'origine et le parcours d'une donnée (source → transformations → usage) pour savoir d'où elle vient et ce qu'elle a subi.
- **LLM (Large Language Model)** `[M7]` — grand modèle de langage généraliste (GPT-4, Mistral, Llama). Puissant, coûteux, opaque.
- **MAE / RMSE** 🎓 `[M4]` — erreurs moyennes en régression (MAE = écart moyen absolu ; RMSE pénalise plus les grosses erreurs).
- **Métadonnée** `[M0/M3]` — donnée qui **décrit** une autre donnée (type, source, date, unité, fraîcheur) ; le catalogue de ce qu'on manipule.
- **MLflow** `[M5]` — outil de **tracking** d'expériences : historiser versions, hyperparamètres et métriques pour comparer les runs. N'est pas un détecteur de drift.
- **MLOps** `[M5]` — pratiques d'industrialisation du ML (CI/CD, monitoring, versionning, réentraînement) ; le DevOps appliqué aux modèles.
- **Model card** `[M7]` — fiche d'identité d'un modèle (tâche, données, limites, biais, métriques). À lire avant d'adopter un modèle.
- **Model Registry** `[M5]` — catalogue versionné des modèles (étapes staging / production). **Optionnel** dans le parcours : le tracking MLflow local suffit.
- **Monitoring** `[M5]` — surveiller un service en production : **en vie ? rapide ? prédit-il toujours bien ?** (via Prometheus + Grafana).

## N — O — P

- **NER (Named Entity Recognition)** `[M2]` — repérer des entités (noms, lieux, n° de sécu) dans du texte ; utile pour la pseudonymisation.
- **ORM (Object-Relational Mapping)** `[M3]` — mapper des tables SQL sur des classes Python (ex. **SQLAlchemy**) pour manipuler la BDD en objets, sans écrire de SQL brut.
- **Outliers (valeurs aberrantes)** `[M2/M3]` — valeurs très éloignées du reste des données : soit un **vrai extrême** à conserver, soit une **erreur de mesure** (capteur défaillant, saisie) à signaler. Une valeur aberrante n'est **pas forcément un signal** (cf. « anomalie ≠ signal ») — à repérer en EDA (boxplot, écart-type, `describe`), pas à supprimer par réflexe.
- **Overfitting (surapprentissage)** 🎓 `[M4]` — le modèle mémorise le jeu d'entraînement et généralise mal sur des données nouvelles.
- **Paramètre** `[M1]` — valeur interne **apprise** pendant l'entraînement (poids, seuils). ≠ hyperparamètre.
- **Parquet** `[M2/M3]` — format de stockage **par colonne** : compact, typage préservé, lecture sélective de colonnes ; ≠ CSV (texte, par ligne, types perdus). Choix de stockage à justifier, pas par défaut.
- **Pipeline (scikit-learn)** `[M2]` — enchaînement reproductible de prétraitements + modèle, en un seul objet persistable.
- **Précision (precision)** 🎓 `[M1]` — parmi les cas prédits positifs, combien le sont vraiment.
- **Prometheus** `[M5]` — outil qui **collecte** les métriques exposées par un service (`/metrics`) pour le monitoring (visualisées dans Grafana).
- **Promotion (conditionnelle)** `[M6]` — ne remplacer le modèle en prod par un réentraîné **que s'il bat l'ancien** sur le jeu de référence. Jamais aveugle.
- **PSI (Population Stability Index)** `[M6]` — indice de stabilité d'une distribution entre deux périodes. < 0.1 stable, 0.1-0.25 suspect, > 0.25 dérive.
- **Pseudo-code** `[M8]` — décrire un composant par ses **signatures + son flux**, sans syntaxe précise ; sert à concevoir sans implémenter.
- **Pseudonymisation** 🎓 `[M2/M3]` — remplacer les identifiants directs pour réduire le risque de réidentification (≠ anonymisation, irréversible).
- **psutil** `[M7]` — librairie Python pour mesurer la consommation d'un process (temps, mémoire RSS) ; sert à **chiffrer** la sobriété.

## R

- **RAG (Retrieval-Augmented Generation)** `[M7]` — brancher un LLM sur **vos** documents : retrouver les passages pertinents et les injecter dans le prompt pour des réponses ancrées.
- **Rappel (recall)** 🎓 `[M1]` — parmi les vrais positifs, combien le modèle en retrouve. Crucial quand rater un positif coûte cher (fraude, panne).
- **Réentraînement (retraining)** `[M6]` — réentraîner un modèle sur des données plus récentes, déclenché sur un **seuil** (dérive mesurée ou volume de feedback).
- **Régression** 🎓 `[M4]` — prédire une **valeur continue** (prix, durée), par opposition à la classification.
- **Réidentification (par croisement)** 🎓 `[M3]` — retrouver une personne en **croisant** plusieurs champs anodins pris isolément (le risque naît du croisement, pas de la colonne seule). Cœur de l'audit RGPD multi-sources (C2 N2).
- **RGPD** 🎓 `[M2]` — règlement européen sur les données personnelles (base légale, minimisation, art. 9 données sensibles, art. 22 décision automatisée).
- **ROC-AUC** 🎓 `[M1]` — mesure la capacité d'un modèle à séparer les classes, indépendamment du seuil.
- **Rollback** `[M5]` — revenir à la version précédente d'un service/modèle après un incident. Procédure clé du runbook.
- **Runbook** `[M5]` — procédures d'astreinte (que faire si le service tombe / ralentit / dérive / doit être rollback).

## S — T

- **Seuil (de décision / de rejet)** `[M1/M7]` — curseur qui transforme une probabilité en décision ; sous le seuil → revue humaine (fallback). Ajustable selon le **coût de l'erreur**, pas une vérité.
- **SLM (Small Language Model)** `[M8]` — petit modèle de langage (1-3B), souvent suffisant et exécutable en local.
- **Sobriété** `[transverse]` — choisir la solution la plus simple/légère qui résout le besoin ; garde-fou central du parcours contre le sur-engineering.
- **SPOF (Single Point of Failure)** `[M7]` — composant unique dont la panne arrête tout le système (ex. modèle sur une seule machine). Risque d'architecture.
- **Split (train/test)** 🎓 `[M1]` — séparer les données pour entraîner d'un côté, évaluer de l'autre. Temporel si l'ordre du temps compte.
- **Token** `[M7]` — unité de texte (≈ ¾ d'un mot) ; les LLM facturent au token (l'output coûte souvent plus que l'input).
- **Transfer learning** `[M4]` — réutiliser un modèle pré-entraîné en n'ajustant que ses dernières couches sur sa tâche.

## V — Z

- **Validation croisée (cross-validation)** 🎓 `[M4]` — évaluer un modèle sur plusieurs découpages pour une mesure plus robuste (KFold, TimeSeriesSplit).
- **Variable sensible** 🎓 `[M2]` — attribut protégé (sexe, âge, origine) dont l'usage peut induire de la discrimination.
- **Vector store** `[M7]` — base indexant des embeddings pour la recherche par similarité (ChromaDB, FAISS).
- **Versionner (un modèle)** `[M5]` — tracer chaque version du modèle (poids + params + métriques) pour comparer et revenir en arrière (tag git, MLflow).
- **Zero-shot** `[M4/M8]` — faire exécuter une tâche par un modèle **sans aucun exemple** d'entraînement.
