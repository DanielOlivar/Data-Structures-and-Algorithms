def intercambia(A,x,y): #recibe los valores de i y j
    tmp=A[x] #variable temporal
    A[x]=A[y] #intercambia 
    A[y]=tmp #intercambia
def particionar(A,p,r): #p primero r ultimo, 
    x=A[r] #A[r] = pivote 
    i=p-1 # i=0-1 entonces i=-1 
    for j in range(p,r): #El ciclo va de 0 a 5, compara los pivotes con cada uno de los elemntos del arreglo, j son los indices del arreglo, no compara el pivote
        if (A[j]<=x): #Compara el pivote con cada numero dentro del indice
            i=i+1 #incrementa i 
            intercambia(A,i,j) #intercambiara los valores j e i
    intercambia(A,i+1,r)  #intercambia, i+1= 4 y r=5
    return i+1 #regresa 4 a la linea 16
def Quicksort(A,p,r): #A arreglo, p primer indice, r ultimo indice
    if (p<r): #valida si hay más de un elemento 
        q=particionar(A,p,r) #recibe A, 0 y 6, invoca a la funcion particionar
        print(A[p:r]) #imprime del indice 0 al indice 5
        Quicksort(A, p, q-1) #se invoca sola la funcion, p=0 q=3
        Quicksort(A, q+1, r)
A=[10,80,30,90,40,50,70] #Aquí comienza el programa
Quicksort(A,0,6) #empieza el funcionamiento del programa, invoca a la funcion quicksort y le envia los parametros, 0 primer indice, 6 ultimo indice
print(A)
    





"""
El método quick sort es el más rapido que el merge sort y bubble sort
Es un algoritmo divide y venceras
El pivote puede ser el ultimo, el primero o el elemnto central

i= 
j=
"""
