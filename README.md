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
[Graphique Temperature sur Consommation](Temperature_Consommation.png) [Graphique Surface sur Consommation](Surface_Consommation.png)

On peut remarquer une tendence haussiere entre la surface et la consommation et une tendence en baisse entre la température et la consommation. 
Donc on consomme plus quand la surface augemente ou quand la température baisse.

## Construction du modèle

Maintenant on va mettre en place une régression linéaire avec la consommation comme variable (Y) et la température extérieure comme variable (X) : 

```
import pandas   
import numpy    
import matplotlib.pyplot as plt 
from scipy import stats

df = pandas.read_csv(r"C:\Users\Abdessamad\Downloads\donnees_consommation.csv") #Bibliothéque de lecture des données
Y = df['Consommation']
Z = df['Surface']
X = df['Temperature']

slope, intercept, r, p, std_err = stats.linregress(X, Y)


def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc, X))

plt.scatter(X, Z)
plt.plot(X, mymodel)
plt.show()

```

Et voici le résultat donnée : [Graphique Temperature sur Consommation avec Regression](Temperature_Consommation_Reg.png)
Ce qui nous donne cette équation : 
- Consommation = -2.6756521139202563 * Température + 283.95837115769524

On peut mettre en place une régression linéaire comme l'exemple d'avant, mais avec la consommation comme variable (Y) et la surface comme variable (X) : 

```
import pandas   
import numpy    
import matplotlib.pyplot as plt 
from scipy import stats

df = pandas.read_csv(r"C:\Users\Abdessamad\Downloads\donnees_consommation.csv") #Bibliothéque de lecture des données
Y = df['Consommation']
X = df['Surface']
Z = df['Temperature']

slope, intercept, r, p, std_err = stats.linregress(X, Y)


def myfunc(x):
    print(slope)
    print (intercept)
    return slope * x + intercept

mymodel = list(map(myfunc, X))

plt.scatter(X, Y)
plt.plot(X, mymodel)
plt.show()

```

Et voici le résultat donnée : [Graphique Surface sur Consommation avec Regression](Surface_Consommation_Reg.png)
Ce qui nous donne cette équation : 
- Consommation = 1.1983392043139784 * Surface + 57.836671718730685

Maintenant on va créer régression linéaire multiple, mais avec la consommation comme variable (Y) et la surface/temperature comme variable (X) : 

```
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"C:\Users\Abdessamad\Downloads\donnees_consommation.csv") #Lecture du CSV

X = df[['Temperature', 'Surface']].values #Variables Temperature/Surface

y = df['Consommation'].values # Variable Consommation

# Régression linéaire multiple
model = LinearRegression()
model.fit(X, y)

# Récupérer les coefficients
a, b = model.coef_   # a pour Temperature, b pour Surface
c = model.intercept_

print(f"Équation : Consommation = {a:.3f} * Température + {b:.3f} * Surface + {c:.3f}")

```
Ce qui nous donne cette équation : 
- Consommation = -2.496 * Température + 1.187 * Surface + 101.886

## Évaluation du modèle

Je modifie le programme au dessus pour connaitre le coefficient de détérmination R2 et l'erreur quadratique moyenne : 

```
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Charger les données
df = pd.read_csv(r"C:\Users\Abdessamad\Downloads\donnees_consommation.csv")

X = df[['Temperature', 'Surface']].values
y = df['Consommation'].values

# Régression
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# MSE et R2
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print("MSE :", mse)
print("R2 :", r2)
print(f"Équation : Consommation = {model.coef_[0]:.3f} * Température + {model.coef_[1]:.3f} * Surface + {model.intercept_:.3f}")

```

Ce qui donne : 
- MSE : 217.9650239723391
- R2 : 0.9623173421499224
- Équation : Consommation = -2.496 * Température + 1.187 * Surface + 101.886
MSE vaut 217.96 donc on a une erreur de 14.8 environ, ce qui est acceptable vu la grandeur de variation de la consommation.
Notre R2 est proche de 1, donc la température et la surface expliquent grandement les variations de consommation.

Donc notre model est assez proche de la réalité !

## Prédiction
On va utiliser notre model pour faire de la prédiction : 
• Quand la température est de 12 °C et la surface de 130 m².

• Quand la température est de 28 °C et la surface de 110 m².
