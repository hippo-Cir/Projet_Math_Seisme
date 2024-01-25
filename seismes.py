import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Partie 1: Les lieux les plus secoués

# 1. Lecture du fichier .csv en Python
seismes_2014 = pd.read_csv('seismes_2014.csv')

# 2. Nombre total de séismes enregistrés en 2014
total_seismes = len(seismes_2014)
print("Nombre total de séismes enregistrés en 2014 :", total_seismes)

# 3. Effectifs des 20 lieux les plus fréquemment secoués
noms = seismes_2014['pays'].value_counts().head(20)
print("Top 20 des lieux les plus fréquemment secoués :\n", noms)

# 4. Boîtes à moustaches pour les 20 lieux les plus fréquemment secoués
top_20 = noms.index.tolist()
top_20_data = seismes_2014[seismes_2014['pays'].isin(top_20)]
plt.figure(figsize=(12, 8))
sns.boxplot(data=top_20_data, x='pays', y='mag')
plt.xticks(rotation=45)
plt.title("Magnitude des séismes dans les 20 lieux les plus fréquemment secoués")
plt.xlabel("Pays")
plt.ylabel("Magnitude")
plt.show()

# Partie 2: Cartes des séismes dans le monde

# 1. Sélection des séismes perceptibles pour l'humain
F = seismes_2014[seismes_2014['mag'] >= 3]
F['m'] = F['mag'].astype(int)

# 2. Carte de chaleur des séismes de magnitude <5
palette = {3: 'hotpink', 4: 'green', 5: 'chocolate', 6: 'blue', 7: 'red', 8: 'black'}
fig = px.density_mapbox(F[F['mag'] < 5], lat='lat', lon='lon', z='mag', radius=10, zoom=1,
                        mapbox_style='carto-positron', center=dict(lat=0, lon=0), opacity=0.5,
                        color_continuous_scale=list(palette.values()), range_color=[3, 8])
df_high_mag = F[F['mag'] >= 5]
fig.add_trace(px.scatter_mapbox(df_high_mag, lat='lat', lon='lon', color='mag',
                                size='mag', size_max=10, color_continuous_scale=list(palette.values()),
                                range_color=[3, 8]).data[0])
fig.show()
