import pandas as pd
import plotly.express as px
# Lecture du fichier CSV
seismes = pd.read_csv('./seismes_2014.csv')

# Sélection des séismes de magnitude supérieure ou égale à 3
F = seismes[seismes['mag'] >= 3]

# Arrondir les valeurs de magnitude à la partie entière
F['m'] = F['mag'].astype(int)

# Afficher les premières lignes de la table F
print(F.head())

# Charger les données des séismes de magnitude <5
df = pd.read_csv('seismes_2014.csv')
df = df[df['mag'] < 5]

# Créer un dictionnaire de la palette de couleurs
palette = {
    3: 'hotpink',
    4: 'green',
    5: 'chocolate',
    6: 'blue',
    7: 'red',
    8: 'black'
}

# Créer la carte de chaleur avec Plotly Express
fig = px.density_mapbox(df, lat='lat', lon='lon', z='mag', radius=10, zoom=1,
                        mapbox_style='mapbox://styles/mapbox/light-v10',
                        center=dict(lat=0, lon=0), opacity=0.5,
                        color_discrete_map=palette, range_color=[3, 8])

# Ajouter les points pour les séismes de magnitude m>=5
df_high_mag = df[df['mag'] >= 5]
fig.add_trace(px.scatter_mapbox(df_high_mag, lat='lat', lon='lon', color='mag',
                                size='mag', size_max=100, color_discrete_map=palette,
                                range_color=[3, 8]).data[0])

# Afficher la carte
fig.show()
