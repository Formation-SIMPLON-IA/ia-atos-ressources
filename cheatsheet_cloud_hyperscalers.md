# Cheatsheet — Cloud & hyperscalers pour l'IA

> **Ressource transverse — culture pure, aucun hands-on.** Réf rapide : *à quoi
> ressemblerait notre chaîne IA si elle tournait chez un fournisseur cloud, et
> comment arbitrer cloud vs self-host*.
>
> **Ancrage parcours** : dans ce parcours on déploie en **local/Docker par choix
> pédagogique** — pour comprendre chaque brique. En entreprise, ces briques
> seraient souvent **managées** chez un hyperscaler (cf. mapping § 6). À mettre
> en regard de la [`cheatsheet_sobriete_couts.md`](./cheatsheet_sobriete_couts.md)
> (coûts) et de la [`cheatsheet_mlops_deploiement.md`](./cheatsheet_mlops_deploiement.md)
> (la chaîne qu'on mappe ici).

---

## 0. Hyperscaler : de quoi on parle

Un **hyperscaler** est un fournisseur cloud à échelle mondiale : datacenters
partout, catalogue de centaines de services, facturation à l'usage. Les trois
dominants : **AWS** (Amazon), **Azure** (Microsoft), **GCP** (Google). Pour
l'IA, ils vendent la même chose à trois étages différents (§ 1) — et c'est cet
étage qui détermine ce que tu gères encore toi-même.

---

## 1. Les 3 étages de l'offre IA cloud

| Étage | Ce que tu loues | Ce que tu gères encore | Exemples |
|---|---|---|---|
| **IaaS** (infrastructure) | une VM, souvent avec GPU | tout : OS, Docker, modèle, API, monitoring — comme en local, mais sur leur machine | EC2 (AWS), VM Azure, Compute Engine (GCP) |
| **Service managé ML** (plateforme) | la chaîne MLOps outillée : entraînement, registry, endpoints, monitoring | ton code et tes données ; l'infra est gérée | **SageMaker** (AWS), **Azure ML**, **Vertex AI** (GCP) |
| **API IA prête à l'emploi** | un modèle déjà entraîné, appelé par requête | rien côté modèle : tu envoies une requête, tu paies au volume | **Bedrock** (AWS), **Azure OpenAI**, **Vertex / Gemini** (GCP) |

> 💡 Ce sont les **mêmes 3 étages** que la décision modèle : entraîner soi-même
> ↔ IaaS ; partir d'un pré-entraîné outillé ↔ managé ; consommer un modèle
> fermé ↔ API. Plus tu montes, moins tu gères — et moins tu **maîtrises**
> (coûts, données, dépendance).

---

## 2. Cloud vs self-host : la grille de critères

| Critère | Penche vers le **cloud** | Penche vers le **self-host** |
|---|---|---|
| **Volumétrie** | charge variable ou en pics (on paie l'usage) | charge stable et prévisible (l'infra fixe s'amortit) |
| **Compétences internes** | pas d'équipe infra/GPU | équipe ops existante (votre profil IT !) |
| **Conformité / souveraineté** | données non sensibles, ou région UE contractuellement verrouillée | données sensibles, exigence de maîtrise complète |
| **Coût** | **OPEX** : récurrent, démarre à ~0, grimpe avec l'usage | **CAPEX** : investissement initial, coût marginal ~nul ensuite |
| **Time-to-market** | démarrer demain | on accepte des semaines de mise en place |

> 💡 Même logique que la [`grille_decision_stockage.md`](./grille_decision_stockage.md) :
> on ne choisit pas le cloud « pour faire moderne » mais sur un **besoin
> constaté** (pic de charge, absence de GPU, délai). Et l'inverse vaut aussi —
> self-host « par principe » sans équipe pour l'opérer est un piège symétrique.

---

## 3. Ordres de grandeur de coûts

- **Instance GPU (IaaS)** : ~**1 à 4 €/h** selon le GPU — soit ~700 à 3 000 €/mois
  si elle tourne en continu. D'où l'importance de l'éteindre (ou du serverless).
- **API LLM** : facturation **au token**, input + output. Pour la méthode
  d'estimation et les repères (API ≈ 10× un modèle classique hébergé), voir
  [`cheatsheet_sobriete_couts.md`](./cheatsheet_sobriete_couts.md) § 2 et § 4 —
  on ne duplique pas ses tableaux ici.
- **Le coût qui surprend** : la facture cloud n'est pas que le compute — stockage,
  **sortie de données** (egress), requêtes, logs. Un POC gratuit devient un
  récurrent à 4 chiffres sans qu'aucune décision n'ait été prise.

---

## 4. Le piège du vendor lock-in

Plus tu montes dans les étages du § 1, plus ton code épouse les APIs
**propriétaires** du fournisseur : un pipeline SageMaker ne se rejoue pas tel
quel sur Vertex AI. Conséquences : migration coûteuse, hausses de tarif
subies, roadmap dépendante du fournisseur.

Parades classiques (culture) : privilégier les **standards portables** (Docker,
MLflow, modèles open-weights), isoler les appels au fournisseur derrière une
interface à soi, et chiffrer le **coût de sortie** avant de signer — pas après.

> 💡 Notre chaîne M5/M6 (FastAPI + Docker + MLflow + Prometheus) est justement
> **portable** : elle tournerait telle quelle sur une VM de n'importe quel
> fournisseur. C'est un choix d'architecture, pas un hasard.

---

## 5. Souveraineté & RGPD

- **Où vivent les données ?** Les hyperscalers proposent des régions UE
  (Paris, Francfort…), mais restent des sociétés **américaines** soumises à
  des lois extraterritoriales (CLOUD Act) — un sujet juridique réel pour des
  données sensibles (santé, défense, secteur public).
- **Alternatives européennes** (culture) : **OVHcloud** et **Scaleway**
  (IaaS/GPU français), **Mistral** (LLM français, API et poids ouverts pour
  certains modèles). Offres moins profondes que les hyperscalers, mais
  argument de souveraineté direct.
- **Réflexe conception** (attendu en M7-M8) : « où sont hébergées les données,
  sous quelle juridiction, et qu'est-ce qui sort vers une API externe ? » fait
  partie de la recommandation — pas une note de bas de page.

---

## 6. Mapping : ce qu'on a fait ↔ l'équivalent managé

Tout ce qu'on a monté à la main en M5/M6 existe en version managée. Savoir
faire la correspondance = parler le langage d'une DSI en entretien :

| Ce qu'on a fait dans le parcours (M5/M6) | L'équivalent managé (AWS / Azure / GCP) |
|---|---|
| API FastAPI + docker-compose | endpoints managés : SageMaker Endpoints / Azure ML Endpoints / Vertex AI Prediction |
| MLflow tracking local (`mlruns/`) | SageMaker Experiments / Azure ML (MLflow intégré) / Vertex AI Experiments |
| CI/CD GitHub Actions | idem, ou CodePipeline / Azure DevOps / Cloud Build |
| Prometheus + Grafana | CloudWatch / Azure Monitor / Cloud Monitoring |
| Dérive PSI/KS calculée à la main | SageMaker Model Monitor / Azure ML data drift / Vertex AI Model Monitoring |
| cron + script de réentraînement | SageMaker Pipelines / Azure ML Pipelines / Vertex AI Pipelines |

> 💡 Aucun de ces services managés n'est utilisé dans le parcours — c'est
> voulu : les gestes faits à la main sont exactement ceux que ces services
> automatisent. Qui a écrit la promotion conditionnelle en script comprend un
> pipeline managé en une heure.

---

## 7. Pour aller plus loin

- **Tarifs GPU (ordres de grandeur)** : https://aws.amazon.com/ec2/pricing/on-demand/ · https://www.ovhcloud.com/fr/public-cloud/prices/
- **Régions et résidence des données** : https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/
- **Mistral (LLM européen)** : https://mistral.ai/
- [`cheatsheet_sobriete_couts.md`](./cheatsheet_sobriete_couts.md) (méthode d'estimation des coûts)

---

## 8. À retenir

- **3 étages** : IaaS (VM+GPU, tu gères tout) → managé ML (SageMaker / Azure ML /
  Vertex AI) → API prête à l'emploi (Bedrock / Azure OpenAI / Gemini). Plus haut
  = moins d'ops, moins de maîtrise.
- **Cloud vs self-host** se décide sur des critères : volumétrie, compétences,
  conformité, OPEX vs CAPEX — pas sur la mode.
- Repères : GPU ~**1-4 €/h** ; API LLM au token (cf. cheatsheet sobriété) ;
  attention aux coûts annexes (egress, stockage).
- **Lock-in** : les étages hauts épousent des APIs propriétaires — standards
  portables (Docker, MLflow) et coût de sortie chiffré avant de signer.
- **Souveraineté** : régions UE ≠ juridiction UE ; alternatives européennes =
  OVHcloud, Scaleway, Mistral.
- Notre chaîne locale M5/M6 a un **équivalent managé ligne à ligne** (§ 6) — la
  compétence acquise se transpose, c'est le but.

---

*Cheatsheet pédagogique ATOS — Cloud & hyperscalers. Culture pure : rien de
cette fiche n'est manipulé dans le parcours.*
