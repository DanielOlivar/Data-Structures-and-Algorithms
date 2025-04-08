#Nusqueda binaria iterativa
import math
def busquedaBinIter(A,x,izquierda,derecha):
    while izquierda<=derecha:
        medio=math.floor((izquierda+derecha)/2) #Da el indice del punto medio
        if (A[medio]==x): #compara el valor medio con el valor del indice mas grande
            return medio
        elif (A[medio]<x): #compara si es menor el valor medio con el valor del indice mas grande
            izquierda = medio+1 #Le da nuevo valor al valor indice mas chico cuando el numero es mas chico que el del indice medio
        else:
            derecha=medio-1 #Le da un nuevo valor al inidce mas grande cuando el numero es mas grande que el del indice medio
    return -1 #Si no se encuentra cuando el numero

A=[0,10,20,30,40,50,60,70,80]
x=80 #valor a encontrar
izquierda=0 #indice mas pequeño 
derecha=8 #indice mas grande
print(busquedaBinIter(A, x, izquierda, derecha)) #impriir el INDICE del valor encontrado
