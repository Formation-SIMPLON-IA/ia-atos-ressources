# Ressources publiques — Parcours IA ATOS

> Repo `ia-atos-ressources` — ressources transverses, partagées entre tous les briefs
> du parcours **« Concevoir et implémenter une solution d'IA »** (CISIA / OPCO ATLAS).

Ce repo est complémentaire au repo `ia-atos-parcours` qui contient les briefs
individuels avec leurs squelettes et mini-cours.

---

## 📁 Contenu

| Fichier | Quand le mobiliser ? |
|---|---|
| `canevas-cas-usage-v2.ipynb` | **Trame du notebook certif M9** — à utiliser comme grille de référence dès M0, sections ouvertes module par module (cf. tableau « Mobilisation » à l'intérieur) |
| `journal-de-bord.ipynb` | **Journal quotidien** à tenir au fil du parcours — sera fusionné avec le canevas en M9 (cf. `merge_for_certif.py` du repo `ia-atos-parcours`) |
| `PlanningSemaineFormation.png` | Planning visuel du parcours — sur quelle semaine quel module |

---

## 🚀 Utilisation pour les apprenants

1. **Clone ce repo une fois** ou utilise les liens directs depuis Simplonline.
2. **Récupère le canevas** dans ton repo perso au démarrage de M0 — tu l'enrichis
   au fur et à mesure que les modules avancent (sections à ouvrir selon le module
   en cours).
3. **Tiens le journal de bord** au quotidien : 1 entrée par jour de formation,
   pas plus de 10 lignes — actions du jour, difficultés, prochain pas.
4. **En M9** : fusion automatique des deux fichiers en un seul notebook certif
   (le script de fusion est dans `ia-atos-parcours/scripts/merge_for_certif.py`).

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
