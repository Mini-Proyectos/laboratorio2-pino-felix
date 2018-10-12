# Sorts.py
# Autor: Luis Pino (15-11138) y Félix Arnos (15-10088)
# Descripcion: Implementacion de los algoritmos InsertionSort y MergeSort
import sys 
# Ordenamiento por inserción
def InsertionSort(A:list,P:int,R:int):
	for j in range (P+1,R):
		key=A[j]  #Elemento a Insertar
		i=j-1
		while (i>=P and A[i]>key):
			A[i+1] = A[i]
			i = i-1
		A[i+1] = key
	return(A)

#Ordenamiento por unión
global arreglo

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

	L=[]
	R=[]

	for i  in range(0,n):
		L.append(i)
		L[i] = arreglo[p+i-1]

	for i  in range(0,m):
		R.append(i)
		R[i] = arreglo[q+i]

	L.append(n+1)
	R.append(m+1)
	L[n+1] = sys.maxsize

	for k in range(p,r):
		if L[i]<=R[j]:
			arreglo[k]=L[i] #Remover primero de L 
			i=i+1
		else:
			arreglo[k]=R[j] #Remover primero de R
			j=j+1