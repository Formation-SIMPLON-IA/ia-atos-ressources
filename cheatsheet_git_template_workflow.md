# Cheatsheet — workflow Git « Use this template » + binôme

> **Ressource transverse — à garder ouverte sur chaque brief de code (dès M1).**
> Réf rapide du **workflow** : du repo template à ta livraison, seul ou en binôme.
>
> Complète [`conventions_commit.md`](./conventions_commit.md) (qui couvre les
> **messages** de commit). Ici on couvre **le cycle** : créer ton repo, démarrer
> proprement, collaborer, et ce qu'on commit (ou pas).

---

## 1. Le cycle « Use this template » (à chaque brief de code)

```
   Repo TEMPLATE du brief (ia-atos-parcours-mX-bY)
        │  clic « Use this template » (bouton vert, GitHub)
        ▼
   TON repo perso : <MX-BY>-<thème>-<prénom>     (sur TON compte GitHub)
        │  git clone
        ▼
   Ton dossier local  ──►  venv + install  ──►  tu travailles  ──►  commits
        │
        ▼
   git push  (chez toi) ──► lien envoyé à la formatrice avant l'échéance
```

> 💡 **« Use this template » ≠ fork.** Le template te crée un repo **neuf et
> indépendant** (pas d'historique lié), sur **ton** compte. Tes commits restent chez
> toi.

---

## 2. Démarrer proprement (les 4 commandes)

```bash
git clone git@github.com:<toi>/<MX-BY>-<thème>-<prénom>.git
cd <MX-BY>-<thème>-<prénom>
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Puis lance le test « hello world » fourni (`pytest -q`) ou le squelette pour vérifier
que tout tourne **avant** de coder.

> 💡 **Identité git** (une fois par machine, si pas déjà fait) :
> ```bash
> git config --global user.name "Ton Prénom Nom"
> git config --global user.email "ton.email@exemple.fr"
> ```
> Sinon tes commits sont mal attribués sur GitHub.

---

## 3. Travailler en binôme (M3-B2, M4-B2, M5, M6, M7-B2, M8-B2)

Un **seul** des deux fait « Use this template », puis ajoute l'autre en
**collaborateur** (Settings → Collaborators). Conventions :

| Convention | Comment |
|---|---|
| **Branches nominatives** | `git checkout -b <prénom>/<feature>` — chacun sa branche, on merge dans `main` |
| **Co-authored-by** | en pair-coding, créditer les 2 auteurs (cf. § ci-dessous) |
| **Coordination** | MP Discord **2 fois/jour** minimum en async (matin + soir) |
| **Test croisé** | avant de livrer, **l'un clone et lance le repo de l'autre** sur sa machine |
| **Répartition** | décider qui fait quoi au démarrage, **switcher** les rôles en cours |

**Créditer les 2 auteurs** sur un commit pair-codé :

```bash
git commit -m "feat(api): add /score endpoint

Co-authored-by: Prénom Nom <email@exemple.fr>"
```

> 💡 La ligne `Co-authored-by:` (précédée d'une **ligne vide**) fait apparaître les
> **2 avatars** sur GitHub. C'est ce qui prouve la collaboration (CT9).

---

## 4. Ce qu'on commit — ce qu'on ne commit JAMAIS

Le `.gitignore` du template gère déjà l'essentiel. À retenir :

| ✅ On commit | 🚫 On ne commit pas |
|---|---|
| code (`src/`, `app/`, `tests/`) | `.venv/`, `__pycache__/`, `*.pyc` |
| `requirements.txt`, `Dockerfile`, `.gitignore` | `.env` et tout **secret** (clé API, mot de passe) |
| README, docs, notebooks **nettoyés** | `.ipynb_checkpoints/` |
| données **toy** (< 1 Mo) | gros datasets → **script de téléchargement** |
| modèle `.joblib` **léger** (< 10 Mo, `compress=3`) | gros modèles → **script `train.py`** |

> 💡 **`git add .` à l'aveugle = piège n°1.** Tu finis par committer ton `.venv` ou
> un `.env`. Préfère `git status -s` puis `git add <fichiers ciblés>`.
>
> ⚠️ Un **secret commité reste dans l'historique** même après suppression. Si ça
> arrive : préviens, on régénère la clé (ne te contente pas d'un `git rm`).

---

## 5. Taguer une release

Quand un livrable est prêt, pose un **tag** (souvent demandé dans les briefs) :

```bash
git tag v1.0.0-prod        # ex. M5 ; M3 -> v0.1.0-pipeline-m3 ; M8 -> v0.1.0-conception
git push origin v1.0.0-prod
```

---

## 6. Le filet quotidien

```bash
git status -s                          # voir ce qui a changé
git add src/preprocess.py              # stager ciblé (pas git add .)
git commit -m "refactor(training): ..."  # message : cf. conventions_commit.md
git push
git log --oneline -5                   # relire ses derniers commits
```

Vise des **commits explicites et fréquents** (un par intention) — les briefs en
demandent en général **au moins 3-4** (ex. `eda` / `training` / `verdict`).

---

## 7. Pièges fréquents

| Piège | Conséquence | Réflexe |
|---|---|---|
| `git add .` à l'aveugle | `.venv`/`.env` committés | `git status -s` + add ciblé |
| Secret dans un commit | fuite persistante dans l'historique | régénérer la clé, prévenir |
| Pas de `Co-authored-by` en binôme | collaboration invisible (CT9) | créditer les 2 auteurs |
| Identité git non configurée | commits « inconnus » sur GitHub | `git config user.name/email` |
| Commits `WIP` / vagues dans `main` | historique illisible | 1 intention = 1 commit clair |
| Gros modèle/dataset committé | repo lourd, clone lent | `.gitignore` + script de téléchargement |
| Notebook non nettoyé (sorties lourdes) | diffs illisibles, repo gonflé | redémarrer le kernel + effacer les sorties avant commit |

---

## 8. À retenir

- **« Use this template » → ton repo perso** (pas un fork), tu travailles chez toi.
- **Démarrer = 4 commandes** (clone, venv, install, test) **avant** de coder.
- **Binôme** : branches nominatives + `Co-authored-by` + **test croisé** du repo.
- **Jamais** committer `.venv`, `.env`, secrets, gros datasets/modèles — `git add`
  **ciblé**, pas `.` à l'aveugle.
- Pour les **messages**, voir [`conventions_commit.md`](./conventions_commit.md).
