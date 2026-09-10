# Fiches de révision — certification CISIA

Quatre fiches (C1, C2, C4, cadre juridique) plus une synthèse anti-confusion,
construites **depuis le référentiel CISIA**. Objectif : le questionnaire (15
questions, 45 min) et la partie cadrage du cas d'usage.

## Deux versions, un seul contenu

| Version | Pour quoi | Comment l'ouvrir |
|---|---|---|
| **`fiches-revision-cisia.html`** | la version de référence : navigation par ancres, recherche plein texte, **auto-tests dont la correction reste cachée tant que vous ne la dépliez pas** | depuis votre clone : double-clic, ou dans l'IDE clic droit → *Open in Browser* |
| **`fiches-revision-cisia.pdf`** | lire hors ligne, sur téléphone, imprimer, annoter | ouvrir le fichier |

> ⚠️ Depuis l'interface GitHub, le bouton *Raw* d'un `.html` affiche le **code
> source**, pas la page. Ouvrez-le depuis votre clone local.

Le PDF est **dérivé** du HTML : même contenu, mais les repères de correction
sont regroupés en **annexe de fin** — sinon les auto-tests se liraient avec la
réponse sous les yeux.

## Comment s'en servir

L'ordre des fiches n'est pas l'ordre de lecture. Priorité :

1. **C4 — Choisir un modèle** : commencez par la section 0 (précision vs rappel).
   C'est le point qui coûte le plus de points, et il ne s'agit pas de vocabulaire.
2. **AI Act & RGPD** : le seul contenu du questionnaire qui ne correspond à aucun
   geste du parcours — donc rien ne le rattrape par l'expérience.
3. **C1 — Identifier un jeu de données**.
4. **C2 — Risques éthiques** : consolidation.
5. **La synthèse** (« les distinctions à ne jamais confondre ») : la dernière
   page à relire avant l'épreuve.

Les auto-tests se font **à voix haute, sans relire**. Plus de dix secondes
d'hésitation sur une question : reprenez la section, ne regardez pas la réponse.

## Régénérer le PDF

Après toute modification du HTML :

```bash
python build_pdf.py          # → fiches-revision-cisia.pdf
```

Dépendance : `weasyprint` (`brew install weasyprint`). Le script détecte le
module Python ou, à défaut, le binaire.
