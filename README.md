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
| [`grille_decision_C4.md`](./grille_decision_C4.md) | **Grille de décision « quel modèle choisir »** — construite collectivement en restitution M4-B1, à enrichir au fil des modules. |
| [`canvas-cas-usage-v2.ipynb`](./canvas-cas-usage-v2.ipynb) | **Trame du notebook certif M9** — à utiliser comme grille de référence dès M0, sections ouvertes module par module (cf. tableau « Mobilisation » à l'intérieur). |
| [`matrice-notebook-initiale.ipynb`](./matrice-notebook-initiale.ipynb) | **Matrice initiale du notebook** — version brute distribuée en amont, à mettre en regard du canvas pour comprendre l'évolution attendue. |
| [`journal-de-bord.ipynb`](./journal-de-bord.ipynb) | **Journal quotidien** à tenir au fil du parcours — sera fusionné avec le canvas en M9 (cf. `merge_for_certif.py` du repo `ia-atos-parcours`). |
| `PlanningSemaineFormation.png` | Planning visuel du parcours — sur quelle semaine quel module. |

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
