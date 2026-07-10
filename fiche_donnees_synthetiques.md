# Fiche — Données synthétiques & augmentation

> **Ressource transverse — culture + un exemple copiable.** Réf rapide :
> *pourquoi et comment générer des données, et pourquoi s'en méfier*.
>
> Mobilisée en **M6** (point flash rééquilibrage / feedback). À mettre en regard
> de la [`cheatsheet_metriques.md`](./cheatsheet_metriques.md) (le déséquilibre
> qui motive SMOTE) et de la
> [`fiche_cycle_vie_donnee.md`](./fiche_cycle_vie_donnee.md) (tracer ce qui est
> généré vs réel).

---

## 0. Pourquoi générer des données ?

Quatre motifs légitimes — chacun avec sa technique :

| Motif | Situation type | Réponse type |
|---|---|---|
| **Rareté** | la classe qui intéresse est rare (fraude ~2 %, panne ~1 %) | rééquilibrage (SMOTE), augmentation |
| **Confidentialité** | données réelles inutilisables (PII, secret métier) | données factices réalistes (Faker) |
| **Rééquilibrage** | le modèle ignore la classe minoritaire | sur-échantillonnage synthétique (SMOTE) |
| **Tests** | tester un pipeline sans attendre les vraies données | génération contrôlée (`make_classification`, Faker) |

---

## 1. Techniques par famille de données

| Famille | Technique | Ce que ça fait | Outil |
|---|---|---|---|
| **Tabulaire** | données factices | lignes réalistes mais inventées (noms, dates, montants) — pour tests et démos, **pas pour entraîner** | Faker |
| **Tabulaire** | rééquilibrage | crée des exemples synthétiques de la classe minoritaire par interpolation entre voisins | **SMOTE** (imblearn) |
| **Tabulaire** | génération contrôlée | dataset jouet aux propriétés choisies (nb classes, bruit, déséquilibre) | `make_classification` (sklearn) |
| **Image** | augmentation | variantes plausibles des images existantes : rotation, flip, crop, luminosité — démultiplie le jeu sans nouvelle collecte | `torchvision.transforms` |
| **Texte** | paraphrase | reformuler les exemples existants (synonymes, modèle de paraphrase) | culture |
| **Texte** | back-translation | traduire FR → EN → FR : le retour est une variante naturelle du texte source | culture |

> 💡 Deux logiques distinctes : **générer du neuf** (Faker, SMOTE — des exemples
> qui n'existent pas) vs **augmenter l'existant** (rotation, paraphrase — des
> variantes d'exemples réels). L'augmentation est plus sûre : elle reste ancrée
> dans des données vraies.

---

## 2. Exemple minimal — SMOTE

```python
# pip install imbalanced-learn   (testé : imblearn 0.14, scikit-learn 1.9)
from collections import Counter
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

# Un jeu déséquilibré : 95 % de classe 0, 5 % de classe 1 (la fraude, la panne…)
X, y = make_classification(n_samples=2000, n_features=10,
                           weights=[0.95, 0.05], random_state=42)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, random_state=42)

print("Avant SMOTE :", Counter(y_train))   # {0: 1420, 1: 80}

smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X_train, y_train)

print("Après SMOTE :", Counter(y_res))     # {0: 1420, 1: 1420}
# On entraîne sur (X_res, y_res)… et on évalue sur (X_test, y_test) INTACT.
```

> ⚠️ **SMOTE sur le train uniquement, jamais avant le split.** Rééquilibrer
> avant de découper injecte des points synthétiques (interpolés depuis le
> train) dans le test → métriques gonflées, fuite. Le jeu de test doit rester
> le monde réel, déséquilibre compris.

---

## 3. Confidentialité différentielle (culture)

Comment publier ou générer des données à partir d'une base réelle **sans
trahir les individus** qui y figurent ? La **confidentialité différentielle**
(differential privacy) est la réponse la plus solide : un bruit calibré est
injecté dans les calculs, de sorte qu'on obtient une **garantie mathématique**
que le résultat serait quasi identique **avec ou sans les données d'une
personne donnée** — impossible donc d'en déduire sa présence dans la base.
C'est ce qu'utilisent des instituts statistiques et de grands acteurs tech
pour publier des agrégats. À connaître comme concept (et comme mot-clé RGPD) ;
aucune mise en œuvre dans ce parcours.

---

## 4. Limites et pièges

| Piège | Conséquence |
|---|---|
| **Synthétique ≠ réalité** | le générateur simplifie ; un modèle brillant sur données synthétiques peut décevoir sur données réelles |
| **Biais copiés, voire amplifiés** | on génère à partir de l'existant : ses biais sont reproduits — et SMOTE peut les densifier |
| **Fuite si mal calibré** | un générateur sur-ajusté peut recracher des individus réels quasi à l'identique (échec de l'anonymisation) |
| **Rééquilibrer masque le vrai problème** | si la classe rare est rare *et mal mesurée*, SMOTE fabrique de la confiance artificielle — parfois la réponse est « collecter mieux » |
| **Test contaminé** | tout ce qui est généré doit rester côté train (cf. § 2) |

---

## 5. Clin d'œil méta

La plupart des datasets de ce parcours (tickets FastIA, dérive simulée
Pyrenex, feedbacks…) sont **synthétiques, générés avec seed fixée**
(`random_state=42`). Ce n'est pas un artifice pédagogique honteux : générer
des données contrôlées et **reproductibles** est une exigence pro — pour
tester un pipeline, simuler une dérive, ou travailler sans exposer de données
réelles. Vous en êtes les consommateurs depuis M0 ; cette fiche vous met de
l'autre côté du générateur.

---

## 6. À retenir

- Quatre motifs : **rareté, confidentialité, rééquilibrage, tests** — chacun sa
  technique (SMOTE, Faker, augmentation, `make_classification`).
- **Générer du neuf ≠ augmenter l'existant** : l'augmentation (rotation,
  paraphrase) reste ancrée dans le réel, c'est la plus sûre.
- **SMOTE : train seulement, jamais avant le split** — le test reste le monde
  réel.
- Confidentialité différentielle = garantie mathématique qu'on ne peut pas
  déduire la présence d'un individu (culture).
- Le synthétique **copie les biais** et ne remplace pas la réalité : c'est un
  outil d'appoint, à tracer comme tel.
- Reproductibilité (**seed fixée**) : la marque d'un générateur pro — comme
  tous les datasets de ce parcours.

---

*Fiche pédagogique ATOS — Données synthétiques & augmentation. Point flash M6.*
