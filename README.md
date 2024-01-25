# Projet CGSI 3: Data Visualization des Données Sismiques

## Préambule
L'Institut d'Études Géologiques des États-Unis (United States Geological Survey, USGS) est un organisme gouvernemental américain dédié aux sciences de la Terre, notamment à la surveillance de l'activité sismique mondiale. Dans le cadre de ce projet, nous utilisons les données fournies par l'USGS pour l'année 2014, extraites et nettoyées du fichier "earthquakes.csv" pour analyser les séismes survenus cette année-là.

## Fichier de données
Le fichier mis à disposition pour ce projet est nommé "séismes_2014.csv". Il contient les informations suivantes pour chaque séisme :
- Instant : date et heure du séisme
- Lat, lon : latitude et longitude de l'épicentre
- Pays : nom du pays ou de l'état
- Mag : magnitude du séisme
- Profondeur : profondeur de l'épicentre

## Objectifs
1. **Top 20 des lieux les plus secoués :** Identifier et analyser les 20 endroits dans le monde où les séismes se produisent le plus fréquemment.
2. **Visualisation de la virulence des tremblements de terre :** Comparer la sévérité des tremblements de terre dans ces 20 lieux à l'aide de graphiques appropriés.
3. **Carte de chaleur dynamique des séismes :** Créer une carte interactive des séismes dans le monde en 2014.
4. **Croisement des données géographiques et de magnitude :** Utiliser une approche similaire à celle de Charles Joseph Minard pour représenter graphiquement les données.

---

## Partie 1: Les lieux les plus secoués

### 1. Lecture du fichier .csv en Python
Utilisez les bibliothèques pandas, pylab et seaborn pour importer, ouvrir et lire le fichier "séismes_2014.csv".

### 2. Nombre total de séismes enregistrés en 2014
Calculer et afficher le nombre total de séismes enregistrés au cours de l'année 2014.

### 3. Effectifs des 20 lieux les plus fréquemment secoués
Construisez une table des effectifs des 20 lieux les plus souvent touchés par les séismes dans le monde. Stockez l'index de cette table dans une variable nommée "noms".

### 4. Boîtes à moustaches pour les 20 lieux les plus fréquemment secoués
Représentez graphiquement les boîtes à moustaches pour la magnitude des séismes dans chacun des 20 lieux. Ceci permettra de comparer la distribution des magnitudes dans ces zones.

---

## Partie 2: Cartes des séismes dans le monde

### 1. Sélection des séismes perceptibles pour l'humain
Créez une table F contenant les séismes de magnitude supérieure ou égale à 3. Pour chaque magnitude, ne conservez que sa partie entière et ajoutez une colonne nommée "m" pour ces valeurs.

### 2. Carte de chaleur des séismes de magnitude <5
Utilisez la bibliothèque Plotly Express avec la palette de couleurs spécifiée pour créer une carte de chaleur des séismes de magnitude inférieure à 5. Ajoutez également les épicentres des séismes de magnitude supérieure ou égale à 5 à la carte.

---

## Partie 3: Carte des séismes façon "Minard"

### 1. Création de la table des effectifs associés à la magnitude
Construisez une table des effectifs associés à la variable "m", prenant ses valeurs entre 3 et 8.

### 2. Réalisation de la carte Minard
Utilisez une approche similaire à celle de Charles Joseph Minard pour créer une carte représentant les données géographiques et de magnitude des séismes.

---

## Partie 4: Utilisation de R et Shiny

Utilisez R et Shiny pour construire une carte interactive des séismes, similaire à celle disponible [ici](https://glowy-earthquakes.glitch.me/?adumkts=social&aduc=social&adum=external&aduca=social_technical&adusf=linkedin&adut=3d76a431-1519-4725-b169-939f5120340f).

---

Ce projet fournit une analyse approfondie des séismes survenus en 2014, avec des visualisations interactives et des représentations graphiques pour mieux comprendre l'activité sismique mondiale. Les instructions fournies dans chaque partie du projet vous guideront à travers les étapes nécessaires pour atteindre les objectifs fixés.
