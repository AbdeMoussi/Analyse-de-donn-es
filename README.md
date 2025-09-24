# Analyse de données
Objectif : Nous avons un jeu de données avec la température, surface et consommation énergétique de 200 lignes. On va explorer les données grâce a des graphiques, construire et évaluer un modèle, faire de la prédiction puis conclure avec des pistes d’amélioration. 

## Exploration des données
Nous devons tout d’abord représenter la consommation par rapport a la température extérieure. Voici le code commenté pour : 

```
import pandas   
import numpy    
import matplotlib.pyplot as plt 

df = pandas.read_csv(r"C:\Users\Abdessamad\Downloads\donnees_consommation.csv") #Lecture du fichier CSV 
X = df['Consommation'] #Sélection de la colonne du CSV, on va chercher les données de celle ci
Y = df['Surface']
Z = df['Temperature']

plt.scatter(X, Z) #On met les points sur le graphique 
plt.show() #On montre le graphique

plt.scatter(X, Y)
plt.show()

```

Ici on affiche les deux graphiques suivants : 
