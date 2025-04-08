def intercambia(A,x,y): #recibe los valores de i y j
    tmp=A[x] #variable temporal
    A[x]=A[y] #intercambia 
    A[y]=tmp #intercambia
def particionar (A,p,r):
    x=A[p]
    i=p
    for j in range (p+1,r+1):
        if(A[j]<=x):
            i=i+1
            intercambia(A,i,j)
    intercambia(A,i,p)
    return i
def QuickSort(A,p,r):
    if(p<r):
        q=particionar(A,p,r)
        print(A[p:r])
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)

A=[10,80,30,90,40,50,70] #Aquí comienza el programa
QuickSort(A,0,6) #empieza el funcionamiento del programa, invoca a la funcion quicksort y le envia los parametros, 0 primer indice, 6 ultimo indice
print(A)