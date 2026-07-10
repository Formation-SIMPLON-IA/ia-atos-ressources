# Cheatsheet — MLOps & déploiement

> **Ressource transverse — à mobiliser dès M5, réutilisée en M6 et M8.** Réf rapide :
> *la chaîne d'industrialisation d'un modèle, et ce qui change par rapport au DevOps
> que tu connais déjà*.
>
> Public **IT** : tu maîtrises déjà Docker, CI/CD, le monitoring. Ce qui est neuf,
> c'est la **couche spécifique au modèle** (versionner, tester, surveiller, réentraîner
> un modèle). Cette cheatsheet relie ce que tu sais au peu qui change. Consolide M5
> (déploiement, CI/CD, monitoring, MLflow) et M6 (dérive, boucle de rétroaction).

---

## 0. MLOps = DevOps + 4 spécificités « modèle »

Le DevOps gère du **code**. Le MLOps gère **code + données + modèle** — trois choses
qui évoluent indépendamment. D'où 4 spécificités qui n'existent pas en DevOps pur :

1. **Le modèle se version** (pas que le code) — un même code + des données différentes = un modèle différent.
2. **Le modèle se teste** différemment — un test unitaire ne dit pas si le modèle *prédit bien* (→ contract test + éval continue).
3. **Le modèle se dégrade tout seul** en prod, sans changement de code — le monde change (→ drift).
4. **Le modèle se réentraîne** — une boucle que le DevOps classique n'a pas.

> 💡 **Bonne nouvelle pour un profil IT** : 80 % du MLOps, c'est du DevOps que tu
> connais. Concentre-toi sur les 4 spécificités ci-dessus.

---

## 1. La chaîne MLOps complète (du commit au réentraînement)

```
   CODE + DONNÉES
        │
        ▼
   [ ENTRAÎNEMENT ]──► modèle.joblib + métadonnées (version, métriques)
        │                     │
        │              tracking MLflow (historise params + métriques)
        ▼
   [ CI/CD ] : tests code → CONTRACT TEST modèle → ÉVAL CONTINUE (seuils)
        │            (release BLOQUÉE si l'éval dégrade)
        ▼
   [ BUILD ] images Docker ──► [ DEPLOY ] docker-compose
        │
        ▼
   [ SERVE ] API (/predict, /health, /metrics)
        │
        ▼
   [ MONITOR ] Prometheus + Grafana : vie / vitesse / qualité
        │
        ▼
   [ DRIFT ] détection (PSI, KS, Chi²) ──► alerte
        │
        ▼
   [ FEEDBACK LOOP ] collecte vrais labels ──► RÉENTRAÎNEMENT
        │                                          │
        └──────── promotion CONDITIONNELLE ◄───────┘
                  (le nouveau modèle ne passe que s'il bat l'ancien)
```

---

## 2. Ta brique DevOps connue → sa spécificité MLOps

| Tu connais (DevOps) | Équivalent / spécificité MLOps |
|---|---|
| Versionner le **code** (Git) | + versionner le **modèle** (`.joblib` + tag, ou MLflow) et **tracer** params/métriques |
| **Tests unitaires** | + **contract test du modèle** (signature d'entrée, sortie déterministe) + **éval continue** (le modèle prédit-il toujours bien ?) |
| **CI/CD** (build, déploiement) | idem + une **étape qui bloque la release si la métrique modèle dégrade** |
| **Monitoring** (CPU, RAM, uptime) | + **monitoring métier** : qualité de prédiction, distribution des sorties |
| **Logs applicatifs** | + **log des prédictions** (pour mesurer la dérive et collecter les vrais labels) |
| **Rien d'équivalent** | **détection de dérive** (le modèle se dégrade sans changement de code) |
| **Rien d'équivalent** | **boucle de réentraînement** + **promotion conditionnelle** |

---

## 3. Les briques ML-spécifiques (détail)

### Versionner & tracer le modèle
- **Minimal** : `joblib.dump(model, ..., compress=3)` + un **tag git** de release + un `.json` de métadonnées (version, métriques, date).
- **Outillé** : **MLflow tracking** (`log_params`, `log_metrics`, `log_model`) → l'UI compare les runs release après release. *Attendu certif.*
- 🚫 Pas besoin d'un **serveur MLflow distant** ni du **Model Registry** au début : le tracking **local** (`mlruns/`) suffit.

### Contract test du modèle
Un test qui vérifie le **contrat** avant déploiement : mêmes colonnes en entrée,
nombre de features de sortie figé, sortie **déterministe**, pas de NaN. Bloque la CI
si rouge. (≠ test « le modèle est bon » — ça, c'est l'éval continue.)

### Évaluation continue
Un script qui **re-mesure les métriques** sur un **jeu de référence figé** à chaque
release et **bloque la release** si dégradation au-delà d'un **seuil** (cf.
[`cheatsheet_metriques.md`](./cheatsheet_metriques.md)). Le code retour non-zéro est
exploité par la CI.

### Monitoring modèle — 3 questions
| Question | Métrique type |
|---|---|
| Le service est-il **en vie** ? | uptime, taux d'erreur, `/health` |
| Est-il **rapide** ? | latence (p50/p95), RPS |
| Prédit-il **toujours bien** ? | distribution des sorties, métrique métier, dérive |

Outils du parcours : **Prometheus** (collecte via `/metrics`) + **Grafana** (dashboard
custom, pas un dashboard importé).

### Détection de dérive (drift)
- **Data drift** : la distribution des entrées change → PSI / KS / Chi².
- **Concept drift** : la relation features→cible change (AUC stable mais perf qui chute).
- Visualisé dans Grafana (panels PSI, métrique dans le temps). cf. M6-B1.

### Boucle de rétroaction & réentraînement
Collecte des **vrais labels** a posteriori → réentraînement **déclenché sur seuil**
(volume ou dérive) → **promotion conditionnelle** : le nouveau modèle ne remplace
l'ancien que s'il le **bat sur le jeu de référence**. Jamais de réentraînement
automatique aveugle. cf. M6-B2.

### Runbook d'astreinte
4 procédures lisibles par un SRE non-data : **Service KO**, **Latence anormale**,
**Métrique modèle dégradée**, **Rollback**. Critère de déclenchement + actions +
responsable pour chacune.

---

## 4. Anti-sur-engineering (ce qu'on met / ce qu'on évite)

| On utilise (suffisant) | On évite au début (sur-engineering) |
|---|---|
| **docker-compose** (orchestration locale) | Kubernetes |
| **MLflow tracking local** (`mlruns/`) | serveur MLflow distant + Model Registry |
| **cron + script** de réentraînement | Airflow / Prefect |
| **Prometheus + Grafana** | stack d'observabilité complète (ELK, Datadog) |
| **SQLite** (logs, feedback) | feature store |

> 💡 La règle [`cheatsheet_sobriete_couts.md`](./cheatsheet_sobriete_couts.md)
> s'applique aussi à l'infra : la brique la plus simple qui résout le besoin. Un
> docker-compose qui tourne bat un Kubernetes à moitié configuré.

---

## 5. Où chaque brique apparaît dans le parcours

| Module | Briques MLOps |
|---|---|
| **M1** | API FastAPI (`/predict`, `/health`), `experiments.md` (intro tracking) |
| **M5-B1** | docker-compose 3 services, CI/CD GitHub Actions, contract test, Prometheus/Grafana, runbook |
| **M5-B2** | MLflow tracking, évaluation continue, blocage de release sur seuil |
| **M6-B1** | détection de dérive (PSI/KS/Chi²), panels Grafana |
| **M6-B2** | boucle de rétroaction, réentraînement, promotion conditionnelle |
| **M8** | conception : pile + déploiement + monitoring (réutilise tout ce qui précède) |

---

## 6. Outils que vous croiserez en entreprise (culture)

Le parcours fait volontairement les gestes **à la main**, avec des briques
simples. En entreprise, les mêmes gestes sont industrialisés par des outils
dédiés — aucun n'est utilisé ici, mais tous se comprennent depuis ce qu'on a fait :

| Outil (entreprise) | À quoi il sert | Ce qu'on fait ici à la place |
|---|---|---|
| **TensorBoard** | visualiser les courbes d'entraînement deep learning (loss/epoch) | rien — sklearn n'a pas de courbes d'epochs |
| **DVC** | versionner les données à l'échelle (Go, jeux qui évoluent) | git suffit : jeux petits et figés |
| **Evidently** | détection de dérive outillée (rapports, dashboards prêts) | PSI / KS à la main — pour comprendre ce que l'outil calcule |
| **Datadog / ELK** | observabilité d'entreprise (logs, APM, alerting unifiés) | Prometheus + Grafana |
| **Airflow / Prefect** | orchestrer des dizaines de jobs interdépendants | cron + script |
| **MLflow Model Registry** | promotion de modèles avec workflow (staging → prod) | tags git + script de promotion conditionnelle |

> 💡 Savoir que ces outils existent et à quoi ils servent = **culture
> d'entretien d'embauche**. Les gestes qu'on a faits à la main sont exactement
> ceux que ces outils industrialisent : qui a calculé un PSI à la main comprend
> Evidently en une heure.

---

## 7. Pour aller plus loin

- **MLOps principles** : https://ml-ops.org/content/mlops-principles
- **Docker Compose** : https://docs.docker.com/compose/
- **GitHub Actions** : https://docs.github.com/actions
- **Prometheus** : https://prometheus.io/docs/introduction/overview/
- **MLflow tracking** : https://mlflow.org/docs/latest/tracking.html

---

## 8. À retenir

- **MLOps = DevOps + 4 spécificités modèle** : versionner, tester (contract + éval),
  surveiller (drift), réentraîner.
- La **chaîne** va du commit au réentraînement, avec une **release bloquée** si la
  métrique modèle dégrade.
- Le **monitoring modèle** répond à 3 questions : en vie ? rapide ? prédit bien ?
- La **promotion** d'un réentraînement est **conditionnelle** — jamais aveugle.
- **Sobriété d'infra** : docker-compose, MLflow local, cron — pas K8s/Airflow/Registry
  tant que le besoin ne l'exige pas.
