# Fiche-pattern — Classer des images (vision)

> Format A4 recto-verso. À garder sous le coude pour M4-B2, réutile en M7-M8.
> Pendant « vision » de la [`fiche_pattern_ML_supervise.md`](./fiche_pattern_ML_supervise.md).
> Le corps illustre le **transfer learning** (le réflexe sobre de l'intégrateur) ;
> pour le **zero-shot** et le **CNN from scratch**, voir l'encart « le delta ».
>
> **Le réflexe sobre** : on **ne réentraîne presque jamais un réseau de zéro**. On
> part d'un modèle **pré-entraîné** (ImageNet), on **gèle le backbone** et on
> n'entraîne qu'une **nouvelle tête** sur nos classes. Résultat correct, peu de
> données, **CPU suffisant** pour de petites images.

---

## La séquence en 6 étapes

```
   [1] Charger images       [2] Explorer (mini)        [3] Découper
   ImageFolder + transforms classes, équilibre,        train / val
   (resize, normalize)      quelques échantillons       (DataLoader)
        │                         │                          │
        └─────────────────────────┴──────────────────────────┘
                                  ▼
   [4] Transfer learning         [5] Évaluer            [6] Persister
   pretrained + FREEZE backbone  accuracy / F1 macro    torch.save(
   + nouvelle TÊTE (n classes)   sur la val               state_dict)
   entraîner la tête seulement
```

| # | Étape | Geste | Clé | Piège typique |
|---|---|---|---|---|
| 1 | **Charger** | images + transforms (resize + **normalisation ImageNet**) | `ImageFolder`, `transforms` | Oublier la normalisation attendue par le modèle pré-entraîné |
| 2 | **Explorer** | nb de classes, équilibre, voir des images | `dataset.classes` | Classes déséquilibrées non vues |
| 3 | **Découper** | train / val (+ `DataLoader`) | `random_split`, `DataLoader` | Pas de séparation → on évalue sur le train |
| 4 | **Transfer** | charger pré-entraîné, **geler**, **remplacer la tête** | `models.resnet18(weights=…)`, `model.fc = nn.Linear(...)` | Réentraîner **tout** le réseau (lent, sur-apprend, inutile) |
| 5 | **Évaluer** | `model.eval()` + `torch.no_grad()` sur la val | `accuracy`, `f1_score(macro)` | Oublier `model.eval()` (BatchNorm/Dropout faussent) |
| 6 | **Persister** | sauver le `state_dict` + la liste des classes | `torch.save(model.state_dict(), …)` | Sauver tout l'objet modèle (fragile) ou oublier l'ordre des classes |

---

### Les 3 invariants à mémoriser

1. **Geler le backbone, n'entraîner que la tête.** `requires_grad = False` sur le
   backbone, et l'optimiseur ne reçoit **que** `model.fc.parameters()`. C'est ce qui
   rend l'entraînement rapide et possible sur **CPU** avec peu de données.
2. **Mêmes transforms à l'entraînement et à l'inférence** (resize + normalisation
   ImageNet identiques). Une image normalisée différemment en prod = prédictions
   fausses, **sans erreur**.
3. **`model.eval()` + `torch.no_grad()` pour évaluer/prédire.** Sinon BatchNorm et
   Dropout restent en mode entraînement et faussent les sorties.

---

## Le squelette minimal qui marche

```python
import torch, torch.nn as nn
from torchvision import models, transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader, random_split

NUM_CLASSES = 7
device = "cuda" if torch.cuda.is_available() else "cpu"   # CPU suffit pour de petites images

# [1] transforms = ce qu'attend le modèle pré-entraîné (taille + normalisation ImageNet)
tf = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])
dataset = ImageFolder("data/images", transform=tf)        # data/images/<classe>/*.png

# [3] Découper train / val
n_val = int(0.2 * len(dataset))
train_ds, val_ds = random_split(dataset, [len(dataset) - n_val, n_val],
                                generator=torch.Generator().manual_seed(42))
train_dl = DataLoader(train_ds, batch_size=32, shuffle=True)
val_dl = DataLoader(val_ds, batch_size=32)

# [4] Transfer learning : pré-entraîné + freeze backbone + nouvelle tête
net = models.resnet18(weights=models.ResNet18_Weights.DEFAULT).to(device)
for p in net.parameters():
    p.requires_grad = False                               # gèle le backbone
net.fc = nn.Linear(net.fc.in_features, NUM_CLASSES).to(device)   # tête entraînable
opt = torch.optim.Adam(net.fc.parameters(), lr=1e-3)      # on n'optimise QUE la tête
crit = nn.CrossEntropyLoss()

for epoch in range(5):                                    # 5 epochs suffisent pour comparer
    net.train()
    for xb, yb in train_dl:
        xb, yb = xb.to(device), yb.to(device)
        opt.zero_grad(); loss = crit(net(xb), yb); loss.backward(); opt.step()

# [5] Évaluer (eval + no_grad)
net.eval(); correct = total = 0
with torch.no_grad():
    for xb, yb in val_dl:
        pred = net(xb.to(device)).argmax(1).cpu()
        correct += (pred == yb).sum().item(); total += len(yb)
print(f"Accuracy val : {correct/total:.3f}")

# [6] Persister (poids + ordre des classes)
torch.save(net.state_dict(), "models/vision_v1.pt")
print("classes :", dataset.classes)   # garde cet ordre pour interpréter les prédictions
```

---

### Comment l'adapter

| Tu veux changer… | Tu modifies… |
|---|---|
| Le backbone | L'étape [4] — `resnet50`, `mobilenet_v3_small` (plus léger), `efficientnet_b0` |
| Le nombre de classes | `NUM_CLASSES` + la tête `nn.Linear(..., NUM_CLASSES)` |
| Affiner un peu plus | Dégeler les **dernières** couches du backbone (fine-tuning partiel, lr plus petit) |
| Les données | L'étape [1] — `ImageFolder("ton_dossier")` (un sous-dossier par classe) |

---

### Les 2 autres options du parcours (le delta)

| Option | Principe | Quand |
|---|---|---|
| **Zero-shot (CLIP)** | aucun entraînement, des **prompts** par classe | **Pas de données labellisées** / MVP rapide — cf. galerie notebook (image) et M4-B2 |
| **CNN from scratch** | entraîner un réseau de zéro | **Rarement justifié** : beaucoup de données + cas très spécifique. Coûteux. |

> 💡 **Garde-fou** : pour un cas industriel typique (peu d'images, classes
> spécifiques), le **transfer learning** est le bon défaut. Le **from scratch** est
> presque toujours du sur-engineering ; le **zero-shot** dépanne quand on n'a pas de
> labels. C'est exactement la comparaison des 3 approches de **M4-B2**.

---

### Quand ça ne marche pas — diagnostic rapide

| Symptôme | Cause probable | Vérifier |
|---|---|---|
| Accuracy val collée au hasard (~1/n classes) | la tête n'apprend pas / backbone non gelé correctement | l'optimiseur reçoit-il `net.fc.parameters()` ? |
| Entraînement très lent | tout le réseau s'entraîne | `requires_grad=False` bien posé sur le backbone ? |
| Bon au train, mauvais en prod (sans erreur) | transforms différentes train/inférence | mêmes `Resize` + `Normalize` partout |
| Prédictions instables d'un appel à l'autre | `model.eval()` oublié | `net.eval()` + `torch.no_grad()` pour prédire |
| `RuntimeError: size mismatch` sur la tête | mauvais `in_features` | `net.fc = nn.Linear(net.fc.in_features, NUM_CLASSES)` |
| Prédiction = mauvaise classe nommée | ordre des classes perdu | réutiliser `dataset.classes` sauvegardé |

---

*Fiche-pattern transverse — classification d'images par transfer learning. Pour le
texte, voir [`fiche_pattern_texte_NLP.md`](./fiche_pattern_texte_NLP.md). Pour le
tabulaire, [`fiche_pattern_ML_supervise.md`](./fiche_pattern_ML_supervise.md).*
