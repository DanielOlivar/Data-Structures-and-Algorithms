def CreaLista(k): #Crea lista de apoyo
    L=[]
    for i in range(k+1): #llega hasta 40
        L.append(0) # L nombre lista, sirve para meter ceros hasta el indice 40
    return L


def CountingSort(A,k):
    C = CreaLista(k)
    B = CreaLista(len(A)-1)
    for j in range(1,len(A)): #Va a contabilizar cuantos numeros iguales hay
        C[A[j]]=C[A[j]]+1
    for i in range(1,k+1): #Realiza la suma de las frecuancias acumuladas
        C[i]=C[i]+C[i-1]
    for j in range(len(A)-1,0,-1): #
        B[C[A[j]]]=A[j]
        C[A[j]]=C[A[j]]-1 #pone los arreglos antes 
    return B

A=[0,9,21,4,40,10,35]
print('Lista Ordenada', CountingSort(A,40))
print('Lista Original', A)


#for in range (inicio, fin -1):
#for in range (inicio, fin, incremento)