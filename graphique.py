import pandas   
import numpy    
import matplotlib.pyplot as plt 

df = pandas.read_csv(r"C:\Users\Abdessamad\Downloads\donnees_consommation.csv") #Bibliothéque de lecture des données
X = df['Consommation']
Y = df['Surface']
Z = df['Temperature']

mymodel = numpy.poly1d(numpy.polyfit(X, Y, 3))
plt.scatter(X, Z)
plt.show()

mymodel1 = numpy.poly1d(numpy.polyfit(X, Y, 3))
plt.scatter(X, Y)
plt.show()
