import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Importer et lire le fichier "seismes_2014.csv"
seismes = pd.read_csv("./seismes_2014.csv")

# 2. Nombre total de séismes enregistrés en 2014
nb_seismes = len(seismes)
print("Nombre total de séismes en 2014 : ", nb_seismes)

# 3. Table des 20 lieux les plus fréquemment secoués dans le monde
top20 = seismes["pays"].value_counts().head(20)
print("Les 20 lieux les plus fréquemment secoués : ")
print(top20)

# 5. Les 6 lieux du monde qui enregistrent les plus fortes magnitudes
top6 = seismes.groupby("pays")["mag"].max().nlargest(6)
print("Les 6 lieux enregistrant les plus fortes magnitudes : ")
print(top6)

# 6. Nombre de séismes de magnitude inférieure ou égale à 2 en Californie et en Alaska
calif_nb = len(seismes[(seismes["pays"] == "California") & (seismes["mag"] <= 2)])
alaska_nb = len(seismes[(seismes["pays"] == "Alaska") & (seismes["mag"] <= 2)])
print("Nombre de séismes de magnitude inférieure ou égale à 2 en Californie : ", calif_nb)
print("Nombre de séismes de magnitude inférieure ou égale à 2 en Alaska : ", alaska_nb)

# Index de la table des 20 lieux les plus fréquemment secoués
noms = seismes["pays"].value_counts().head(20).index

# 4. Boîte à moustaches de la magnitude pour les 20 lieux les plus fréquemment secoués
plt.figure(figsize=(10,7))
sns.boxplot(data=seismes[seismes["pays"].isin(noms)], x="pays", y="mag", whis=10, order=noms)
plt.title("Magnitude des séismes pour les 20 pays les plus fréquemment secoués")
plt.xlabel("Pays")
plt.ylabel("Magnitude")
plt.xticks(rotation=45)
plt.show()
