#Primero - Instalar libreria/paquete/dependencia/biblioteca
#Importar la biblioteca en donde se vaya a usar
#Usar la bibilioteca

import geopandas as gpd
import matplotlib.pyplot as plt

#En python todo es un objeto:
#Atributos
#Comportamientos

#Un geodata frame es una tabla de datos donde al menos una de sus columnas contiene datos espaciales
#Datos espaciales vectoriales (geometricos) puntos/lineas/poligonos

#Leer archivos que tengan datos espaciales
#Ejemplo: Los archivos GeoJSON

archivo = gpd.read_file("custom.geojson")

print(archivo.head())

#archivo.plot()
#plt.show

#archivo.plot()
#plt.savefig("mapa.png", dpi=300, bbox_inches="tight") 
#Exporta el grafico generado como un archivo PNG llamado mapa.png
#El parametro dpi=300 asegura que tenga alta resolucion
#bbox_inches="tight" ajusta los margenes para que nada del mapa quede recortado
#plt.show()

print(archivo.crs) #Sistema de coordenadas

print(archivo.geometry) #Geometria (Poligonos, etc.)

print(archivo.columns[0]) #Columnas o columnas de la tabla

#Imprimir uno por uno los nombres de las columnas
for x in range(0,169):
    print(archivo.columns[x])

#Imprimir los nombres en español de los paises (name_es)
print(archivo["name_es"])

#Mostrar en pantalla el poligono de colombia
colombia = archivo[archivo["name_es"] == "Colombia"]
colombia.plot()
plt.show()