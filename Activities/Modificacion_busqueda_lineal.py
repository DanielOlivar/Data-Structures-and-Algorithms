#Axel Daniel Becerril Olivar
def busquedaLinealRecuriva (A,x,st,end): #st indice menor, end indice mayor
    encontrado=-1 #valor por default para encontrado
    if st > end: #
        return -1
    else:
        for a in range(0,1):
            if A[st] == x: #Compara el indice con el valor a encontrar
                A[a] =st
                print("\n",A[a])
        else:
            return busquedaLinealRecuriva(A, x, st+1, end) #aumenta de indice para comparar un nuevo valor
        return encontrado

A=[3,3,2,55,3,8,3]
x=3 #Valor a encontrar
print(busquedaLinealRecuriva(A, x, 0, 6)) 