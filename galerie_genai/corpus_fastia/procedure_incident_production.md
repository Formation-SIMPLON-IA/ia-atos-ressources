# Procédure de gestion des incidents de production

## Niveaux de sévérité

| Niveau | Définition | Prise en charge |
|---|---|---|
| **P1** | Service client à l'arrêt, perte de données possible | Astreinte mobilisée sous **15 minutes**, 24/7 |
| **P2** | Dégradation majeure, contournement possible | Sous 1 heure, heures ouvrées étendues |
| **P3** | Anomalie gênante sans impact critique | Sous 1 jour ouvré |
| **P4** | Demande ou anomalie mineure | Backlog, priorisé en comité hebdo |

## Déroulé d'un P1

1. Ouverture du **pont d'incident** (canal dédié + visio permanente) ;
2. Un **pilote d'incident** unique est nommé — il communique, il ne débogue pas ;
3. Point de situation toutes les **30 minutes** vers le client ;
4. Toute action en production est tracée dans le journal d'incident.

## Après l'incident

Un **postmortem sans blâme** est rédigé sous **5 jours ouvrés** : chronologie,
cause racine, actions correctives datées et assignées. Il est partagé à
l'équipe et archivé dans l'espace projet.
