#Se importo la libreria math para hacer el seguimiento de las distancias punto a punto
import math

#Definicion de los puntos en tuplas
p1 = (1,2)
p2 = (5,4)
p3 = (-3,-4)
p4 = (2,1)
p5 = (6,-2)

#Agrupacion de los puntos en una lista
puntos = [p1, p2, p3, p4, p5]

distancias = []#Array vacio para las distancias

#iteracion sobre los puntos con bucle for
for punto in puntos:
    x, y = punto #puntos en coordenadas cartesianas
    distancia = math.sqrt(x**2 + y**2)#Calculo de la distancia al origen
    distancias.append(distancia)#se agrega la distancia al array
    print(f"Distancia del punto {punto} al origen: {distancia:.2f}\n")#Imprime el resultado

#Se establece la distancia mínima y el índice del punto correspondiente
distancia_minima = min(distancias)
indice = distancias.index(distancia_minima)#Se obtiene el índice del punto más cercano
#Impresion del punto mas cercano al origen con su distancia minima
print(f"El punto más cercano al origen es: {puntos[indice]} con distancia {distancia_minima:.2f}")