# Sorts.py
# Autor: Luis Pino (15-11138) y Félix Arnos (15-10088)
# Descripcion: Implementacion de los algoritmos InsertionSort y MergeSort

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
