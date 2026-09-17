# Compte rendu — Projet Meridian, comité d'avril

**Client** : Meridian Assurances · **Équipe FastIA** : 4 consultants
**Objet** : migration de l'API de scoring vers la nouvelle plateforme

## Avancement

- Reprise des 3 endpoints historiques terminée, tests de contrat verts ;
- Migration de la base de référentiels réalisée à 80 % ;
- Documentation d'exploitation relue par l'équipe run du client.

## Décisions

- **Passage en recette client le 15 mai** (décision validée par le comité) ;
- Gel des évolutions fonctionnelles jusqu'à la fin de la recette ;
- Ajout d'un consultant FastIA en renfort sur les tests de charge.

## Risques suivis

- **Latence** de l'endpoint de scoring en pic (p95 à 480 ms, cible 300 ms) :
  plan d'optimisation en cours, revue au prochain comité ;
- Disponibilité tardive des jeux de données anonymisés côté client.

## Prochain comité

Le 12 mai, avec démonstration de bout en bout en environnement de recette.
