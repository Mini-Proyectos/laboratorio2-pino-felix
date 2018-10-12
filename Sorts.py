# CI2692 - Laboratorio de Algoritmos y Estrcuturas 2
# Laboratorio 2 - Merge Sort
# Sorts.py
# Autor: Luis Pino (15-11138) y Félix Arnos (15-10088)
# Descripcion: Implementacion de los algoritmos InsertionSort y MergeSort

#	Librerias
global arreglo
import sys

#	Funciones
def InsertionSort(A:list,P:int,R:int):
	for j in range (P+1,R):
		key=A[j]  #Elemento a Insertar
		
		i=j-1 #Definimos la posisción correcta donde debe ser insertado el elemento 

		while (i>=P and A[i]>key):
			A[i+1] = A[i]
			i = i-1
		
		A[i+1] = key 

	return(A) #Dado que InsertioSort es una función, retornamos el valor agregado

def MergeSort(A:list, p:int , r:int ):
	global arreglo
	arreglo = A 
	
	if (p < r):
		q = (p+r)//2  #q es la mitad del arreglo
		MergeSort(arreglo, p, q) #Se realiza mergeSort desde el primer elemento p hasta la mitad del arreglo q
		MergeSort(arreglo, q+1, r) #Se realiza mergeSort desde el elemento q+1 haasta el ultimo elemento r
		Merge(arreglo, p, q, r) #Intercala los elementos que se dividieron 

	return(arreglo)

def Merge(A:list, p:int, q:int, r:int):
	global arreglo
	n = q-p+1   #Tamaño de arreglo[p...q]
	m = r-q   #Tamaño de arreglo[q+1...r]

	#Declaramos nuestros arreglos auxiliares y luego les asignamos los valores correspondientes de nuestro arreglo princiapal
	L=[] 
	R=[]
	for i  in range(0,n):
		L.append(arreglo[p+i-1]) #En cada posición insertamos el valor correspondiente
	for i  in range(0,m):
		R.append(arreglo[q+i]) #En cada posición insertamos el valor correspondiente

	# Asignamos los Sentinelas usando la librería SYS y la funcion maxsize que contiene el tamaño mas grande que puede tener
	# un arreglo en python, representado como un numero entero positivo muy grande
	L.append(sys.maxsize)
	R.append(sys.maxsize)

	i,j=0,0 #Declaramos nuestras variables auxiliares en el valor inicial de ambos arreglos

	for k in range(p,r):
		if L[i]<=R[j]:
			arreglo[k]=L[i] #Removemos el primero de L 
			i=i+1
		else:
			arreglo[k]=R[j] #Removemos el primero de R
			j=j+1

	# Dado que Merge es trabajado como un procedimiento y no como una función, no tiene Return. Esto se hace porque se esta
	# utilizando un arreglo global durante toda el programa para que los cambios registrados sean accesibles a traves de todas
	# las funciones