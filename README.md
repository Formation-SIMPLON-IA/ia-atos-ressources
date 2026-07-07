# Ressources publiques — Parcours IA ATOS

> Repo `ia-atos-ressources` — ressources transverses, partagées entre tous les briefs
> du parcours **« Concevoir et implémenter une solution d'IA »** (CISIA / OPCO ATLAS).

Ce repo est complémentaire au repo `ia-atos-parcours` qui contient les briefs
individuels avec leurs squelettes et mini-cours.

---

## 📁 Contenu

| Fichier | Quand le mobiliser ? |
|---|---|
| [`00_competences_referentiels.md`](./00_competences_referentiels.md) | **Source de vérité des compétences** — 9 C techniques (CISIA) + 9 CT transversales (OPCO ATLAS) avec intitulés officiels, niveaux Simplon et mapping par module. À garder sous la main pendant tout le parcours. |
| [`recap_M0_vers_M1.md`](./recap_M0_vers_M1.md) | **Pont entre M0 et M1** — cycle ML, technos vues vs à venir, compétences cochées. À lire entre vendredi soir M0 et mardi 9h M1. |
| [`panorama_modeles_ML.md`](./panorama_modeles_ML.md) | **Carte du territoire ML** — qu'est-ce qu'un modèle, les 5 grandes familles supervisées tabulaires, vision/texte/LLM. À lire avant M1, réutilisé jusqu'en M8. **Ne pas confondre avec la grille C4** : ici on **situe**, en M4 on **choisit**. |
| [`panorama_huggingface_hub.md`](./panorama_huggingface_hub.md) | **Utiliser un modèle pré-entraîné** — le Hub, les model cards, l'API `pipeline()`, la checklist d'adoption (licence/taille/tâche) et le filtre sobriété. Dès M4-B2, réutilisé en M7-M8. Le geste d'intégrateur par excellence. |
| [`panorama_genai_llm_rag_agents.md`](./panorama_genai_llm_rag_agents.md) | **Carte GenAI** — situer LLM / SLM / RAG / agents, *quand c'est pertinent et quand c'est du sur-engineering*. Arbre de décision « ai-je besoin de GenAI ? » + glossaire express. Amorcé en M4-B2, central en M7-M8. |
| [`glossaire_IA.md`](./glossaire_IA.md) | **Glossaire vivant** — vocabulaire data/IA démystifié (1-2 lignes/terme), tagué par module, 🎓 sur les termes du questionnaire C1/C2/C4. À garder ouvert dès M0, enrichi à chaque module. |
| [`fiche_pattern_ML_supervise.md`](./fiche_pattern_ML_supervise.md) | **Fiche-pattern A4 « entraîner un modèle »** — la séquence en 6 étapes (classification + delta régression), un squelette qui tourne, les 3 invariants et un diagnostic rapide. À garder sous le coude de M1 à M6, et à mobiliser sur chaque notebook de la galerie. |
| [`fiche_pattern_texte_NLP.md`](./fiche_pattern_texte_NLP.md) | **Fiche-pattern A4 « classer du texte »** — séquence en 6 étapes (TF-IDF + LogReg, le réflexe sobre), squelette validé, le delta zero-shot / NER. Dès M2-B2, réutile en M8. |
| [`fiche_pattern_anonymisation_PII.md`](./fiche_pattern_anonymisation_PII.md) | **Fiche-pattern A4 « anonymiser du texte libre (PII) »** — regex AVANT NER, squelette spaCy+regex validé, table des 4 stratégies (redaction/substitution/hash/généralisation), diagnostic des pièges réels. Dès M2-B2, réutile en M3 (RGPD) et M7 (NLP). |
| [`fiche_pattern_vision.md`](./fiche_pattern_vision.md) | **Fiche-pattern A4 « classer des images »** — transfer learning (geler le backbone + nouvelle tête), squelette validé (ResNet18, CPU), le delta zero-shot CLIP / from scratch. Pour M4-B2, réutile en M7-M8. |
| [`galerie_reentrainement/`](./galerie_reentrainement/) | **Étagère asynchrone optionnelle post-M1-B1** — 4 notebooks à autonomie croissante (santé, immobilier, diabète à compléter, vin autonome) pour ancrer le geste « entraîner un modèle » (C5) par la répétition. Pas de livrable, pas de note. |
| [`galerie_modeles_pretraines/`](./galerie_modeles_pretraines/) | **Étagère asynchrone optionnelle dès M4-B2** — pendant « intégration » de la galerie de réentraînement : 4 notebooks (sentiment, tri zero-shot, similarité, anonymisation NER) pour ancrer le geste « **utiliser un modèle pré-entraîné** » (HuggingFace), avec fil rouge sobriété. CPU, modèles légers FR. Pas de livrable. |
| [`conventions_commit.md`](./conventions_commit.md) | **Format des messages de commit** — type, scope, description + exemples. À garder ouvert pendant les briefs avec rendu Git. |
| [`cheatsheet_git_template_workflow.md`](./cheatsheet_git_template_workflow.md) | **Workflow Git « Use this template » + binôme** — du repo template à ta livraison : créer ton repo, démarrer en 4 commandes, branches nominatives + Co-authored-by, ce qu'on commit (ou pas), taguer une release. Complète les conventions de commit. Dès M1. |
| [`grille_decision_C4.md`](./grille_decision_C4.md) | **Grille de décision « quel modèle choisir »** — construite collectivement en restitution M4-B1, à enrichir au fil des modules. |
| [`grille_decision_stockage.md`](./grille_decision_stockage.md) | **Grille de décision « stockage & échelle »** — où/comment stocker les données (relationnel / document / fichier / vectoriel) et quand un outillage lourd (Spark/DWH) se justifie. Compagnon de la grille C4, mobilisée dès M3. |
| [`fiche_cycle_vie_donnee.md`](./fiche_cycle_vie_donnee.md) | **Cycle de vie & lignage de la donnée** — le flux collecte → préparation → entraînement → prod → feedback → oubli, la traçabilité (« quel modèle entraîné sur quelles données ? »), le versionnement des jeux, contrat de données + fiche modèle (M3-B2), RGPD express. Mobilisée en M5 (documentation), M7-B1 (audit) et dans le journal de bord certif. |
| [`fiche_donnees_synthetiques.md`](./fiche_donnees_synthetiques.md) | **Données synthétiques & augmentation** — pourquoi générer (rareté, confidentialité, rééquilibrage, tests), techniques par famille (Faker/SMOTE tabulaire, augmentation image, paraphrase texte), limites et pièges. Exemple SMOTE copiable. Point flash M6. |
| [`cheatsheet_metriques.md`](./cheatsheet_metriques.md) | **Cheatsheet métriques** — quelle métrique pour quel problème (classif / régression / ranking), comment la lire, les pièges (accuracy sur déséquilibré, R² seul, fuite). Consolide M1 + M4 + M6 ; sert C8 et le questionnaire C4. À garder ouverte de M1 à M9. |
| [`cheatsheet_sobriete_couts.md`](./cheatsheet_sobriete_couts.md) | **Cheatsheet sobriété & coûts** — le garde-fou central : mesurer (psutil), estimer un coût LLM, repérer les coûts cachés, arbitrer *sobre vs impressionnant*, « justifier ce qu'on n'a pas mis ». Consolide M4-B2 + M7 + M8. |
| [`cheatsheet_mlops_deploiement.md`](./cheatsheet_mlops_deploiement.md) | **Cheatsheet MLOps & déploiement** — la chaîne du commit au réentraînement, et ce qui change vs le DevOps que tu connais (versionner/tester/surveiller/réentraîner un modèle). Relie chaque brique DevOps connue à sa spécificité MLOps. Dès M5, réutilisé M6/M8. |
| [`cheatsheet_cloud_hyperscalers.md`](./cheatsheet_cloud_hyperscalers.md) | **Cheatsheet cloud & hyperscalers pour l'IA** — culture pure (aucun hands-on) : les 3 étages IaaS / managé ML / API prête à l'emploi, cloud vs self-host, ordres de grandeur, lock-in, souveraineté UE. Mapping « ce qu'on a fait en M5/M6 ↔ l'équivalent managé ». Utile dès M5, surtout M7-M8. |
| [`canvas-cas-usage-v2.ipynb`](./canvas-cas-usage-v2.ipynb) | **Trame du notebook certif M9** — à utiliser comme grille de référence dès M0, sections ouvertes module par module (cf. tableau « Mobilisation » à l'intérieur). |
| [`matrice-notebook-initiale.ipynb`](./matrice-notebook-initiale.ipynb) | **Matrice initiale du notebook** — version brute distribuée en amont, à mettre en regard du canvas pour comprendre l'évolution attendue. |
| [`journal-de-bord.ipynb`](./journal-de-bord.ipynb) | **Journal quotidien** à tenir au fil du parcours — sera fusionné avec le canvas en M9 (cf. `merge_for_certif.py` du repo `ia-atos-parcours`). |
| `PlanningSemaineFormation.png` | Planning visuel du parcours — sur quelle semaine quel module. |

---

## 📄 Série de fiches ML (PDF A4 paysage, imprimables)

12 aide-mémoire qui suivent le cycle réel d'un projet ML — **cadrer & choisir →
préparer → entraîner & évaluer → fiabiliser & comprendre → industrialiser**.
Chaque fiche est autonome ; commencez par le sommaire. Fil rouge : commencer
simple, évaluer honnêtement, ne pas sur-ingénierer.

| # | Fiche | Contenu | Modules |
|---|---|---|---|
| — | [`00_sommaire_serie_ML.pdf`](./00_sommaire_serie_ML.pdf) | La carte de la série : comment les 12 fiches s'articulent | Tout le parcours |
| 1 | [`fiche_choix_famille_ML.pdf`](./fiche_choix_famille_ML.pdf) | Les 4 voies (ML classique, deep, GenAI, renforcement) + arbre de décision tabulaire | M0, M4, M8 |
| 2 | [`cheatsheet_algos_ML_FR.pdf`](./cheatsheet_algos_ML_FR.pdf) | Catalogue des familles d'algos par type de problème : forces, limites, cas d'usage | M1, M4 |
| 3 | [`fiche_preprocessing.pdf`](./fiche_preprocessing.pdf) | Scaling, encodage, manquants, dates — tout dans un pipeline, sans fuite | M2, M3 |
| 4 | [`fiche_stockage_donnees.pdf`](./fiche_stockage_donnees.pdf) | CSV / Parquet / base : choisir selon qui consomme la donnée | M3, M8 |
| 5 | [`aide_memoire_M1.pdf`](./aide_memoire_M1.pdf) | Le workflow entraîner & évaluer de bout en bout + métriques de classification | M1, M5, M6 |
| 6 | [`fiche_validation_reglage.pdf`](./fiche_validation_reglage.pdf) | Train/validation/test, validation croisée, GridSearch — test scellé | M1, M4, M6 |
| 7 | [`fiche_biais_variance.pdf`](./fiche_biais_variance.pdf) | Sur/sous-apprentissage : diagnostiquer l'écart train/validation et corriger | M1, M4 |
| 8 | [`fiche_metriques_regression.pdf`](./fiche_metriques_regression.pdf) | MAE, RMSE, R², MAPE : laquelle choisir et les pièges | M4, M7 |
| 9 | [`fiche_desequilibre_classes.pdf`](./fiche_desequilibre_classes.pdf) | Métriques adaptées, class_weight, SMOTE, seuil de décision | M1, M6 |
| 10 | [`fiche_interpretabilite_xai.pdf`](./fiche_interpretabilite_xai.pdf) | Feature importance, SHAP, LIME, PDP — expliquer les prédictions (AI Act) | M7, M8 |
| 11 | [`fiche_notebook_a_prod.pdf`](./fiche_notebook_a_prod.pdf) | Versionner → packager → servir → monitorer ; le drift et la boucle | M5, M6 |
| 12 | [`fiche_genai_llm_agents.pdf`](./fiche_genai_llm_agents.pdf) | L'échelle prompt → RAG → fine-tuning → agent, et les pièges GenAI | M7, M8 |
| ➕ | [`fiche_techniques_rag.pdf`](./fiche_techniques_rag.pdf) | Annexe de la fiche 12 — améliorer chaque étape du pipeline RAG (chunking, recherche hybride, re-ranking, évaluation récupération/génération) + table symptôme → technique | M7-B2, M8-B2 |

---

## 🚀 Utilisation pour les apprenants

1. **Clone ce repo une fois** ou utilise les liens directs depuis Simplonline.
2. **Garde [`00_competences_referentiels.md`](./00_competences_referentiels.md)
   ouvert dès le démarrage** — il te dit où tu vas et quelles compétences tu
   travailles à quel niveau.
3. **Récupère le canvas** dans ton repo perso au démarrage de M0 — tu l'enrichis
   au fur et à mesure que les modules avancent (sections à ouvrir selon le module
   en cours).
4. **Tiens le journal de bord** au quotidien : 1 entrée par jour de formation,
   pas plus de 10 lignes — actions du jour, difficultés, prochain pas.
5. **En M9** : fusion automatique du canvas et du journal en un seul notebook
   certif (le script de fusion est dans
   `ia-atos-parcours/scripts/merge_for_certif.py`).

---

## 🔄 Mise à jour

Ce repo évolue moins vite que `ia-atos-parcours`. Les changements probables :

- Ajout de **cheatsheets transverses** (ML metrics, Docker compose, Git rebase) au
  fil du parcours.
- Mise à jour du planning si la promo a des aléas calendaires.

Tu peux faire `git pull` au début de chaque module pour récupérer les éventuelles
nouveautés.

---

## 📜 Licence & statut

Repo de travail pédagogique, usage interne formation ATOS Atlas IA. Pour toute
réutilisation extérieure, contacter la formatrice.
