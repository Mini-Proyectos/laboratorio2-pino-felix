# TestSorts.py
# Autor: Luis Pino (15-11138) y Félix Arnos (15-10088)
# Descripcion: Implementacion de un programa de prueba para los algoritmos InsertionSort y MergeSort

#Librerías
import time
import sys
import random
from Sorts import InsertionSort
from Sorts import MergeSort

sys.argv #Recibimos directo de la consola la función y el numero delelementos que tendrá el arreglo

#Funciones
def ArregloRandom (Tamaño:int):
    Arreglo=[]
    for i in range (0,Tamaño):
        Arreglo.append(i)
        Arreglo[i]=random.randint(0,1000)
    
    return Arreglo

#Main
#Creamos el arreglo al azar del tamaño solicitado
TamañoMain=int(sys.argv[2])
Algoritmo=str(sys.argv[1])

#Creamos el arreglo de numeros a ser evaluado
Arreglo=ArregloRandom(TamañoMain)

#Ejecutamos el ordenamiento solicitado
if (Algoritmo=="InsertionSort"):
    inicio=time.time()
    ordenado = InsertionSort(Arreglo,0,TamañoMain)
    fin=time.time()
elif (Algoritmo=="MergeSort"):
    inicio=time.time()
    ordenado = MergeSort(Arreglo,0,TamañoMain)
    fin=time.time()
else:
    print("Este algoritmo de busqueda no está implementado en este programa")

#Tiempo
tiempoTranscurrido=(fin-inicio)*1000

#Salida
print(Algoritmo,TamañoMain,tiempoTranscurrido)
