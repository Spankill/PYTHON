import pandas as pd
import matplotlib.pyplot as plt 

#cargar el dataset
datos = pd.read_csv("D:\ARUHIZA-DEV LANGUAGES PROJECTS\PYTHON\PYTHON\entorno_oficial\Advanced.csv")

#mostrar unas cuantas filas
print(datos.head())

#Ver informacion basica del dataset
print(datos.info())

#estadisticas descriptivas
print(datos.describe())

#Filtar datos (ejm: jugasdores con mas de 20 puntos por partido)
player_28 = datos[datos['age'] > 28]
print (player_28)

#Filtro de jugadores laterales
jugadore_aleros = datos[datos['pos' == 'SF']]


#histograma dede jugadores filtrado (EDADES)s

plt.hist(player_28['age'], bins=10, edgecolor='black')
plt.title('distribucion de EDADES (mayores a 28)')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()



