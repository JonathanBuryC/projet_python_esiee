# Projet Python de Jonathan et Mattéo

## Objectif
**Comprendre le marché mondial d'EDF.**

## Analyse Initiale des Données
Dans ce travail de data science, nous nous sommes amusés à récupérer le dataframe de l'entreprise **EDF** pour étudier son marché au niveau mondial. 

### Production d'Énergie par EDF (2019-2022)
Nous avons dans un premier temps produit un histogramme détaillant la production d'énergie par EDF de 2019 à 2022 selon la filière. **La production nucléaire est prédominante**, avec une moyenne de 140k GWh par année.

### Production d'Énergie par Pays Client
Nous avons ensuite créé un histogramme pour visualiser la production d'énergie par pays client d'EDF selon la filière. La France est le principal bénéficiaire, suivie de près par l'Italie, le Brésil, les USA et l'Angleterre.

## Interrogations et Analyses Supplémentaires
Face à une baisse de la production d'énergie mondiale d'EDF (de 588k GWh en 2019 à 457,6k GWh en 2022), nous avons exploré diverses causes potentielles telles que conflits, concurrence, problèmes de matières premières, politiques des pays, et émissions de CO2.

### Vérification des Données via une API
Pour assurer l'exactitude des données, nous avons analysé la production de CO2 d'EDF pour chaque pays, en utilisant une API : [API EDF](https://opendata.edf.fr/explore/dataset/emissions-de-co2-consolidees-par-pays-du-groupe-edf/api/?disjunctive.perimetre_spatial&sort=-tri). Les résultats obtenus corroborent les données de production d'énergie.

## Visualisation Avancée des Données
Pour une meilleure compréhension, nous avons créé une **carte chloropleth**. Cela a nécessité l'utilisation du dataframe **ISO 3166-1** avec la notation "alpha-3", permettant à Plotly de représenter correctement les pays.

### Comparaison avec l'Histogramme des Pays Clients
La carte chloropleth corrobore les données de notre second histogramme sur la production d'énergie par pays client selon la filière.

## Conclusion
Notre projet a révélé la complexité et les dynamiques du marché mondial d'EDF. Grâce aux outils de data science et de visualisation, nous avons non seulement confirmé la prédominance du nucléaire dans la production d'EDF, mais aussi validé l'intégrité des données d'EDF à travers différentes analyses et visualisations, dont une carte chloropleth innovante et l'exploitation d'une API.
