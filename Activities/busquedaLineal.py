def busquedaLineal(A,n,x):  #N indice mayo, A arreglo, x valor que queremos encontrar
    encontrado=-1 #Indica que no se encontro el valor
    for k in range (n+1): #itera desde 0 a n+1, en este caso sería 5+1 = 6
        if A[k]==x: #Hace las comparaciones, k es el indice que va haciendo el recorrido
            encontrado =k #k tomara el valor del indice en donde esta el numero a encontrar
    return encontrado #regresará el valor de 5 (en donde esta el numero a encontrar)

A=[1,4,6,8,9,11] #Arreglo de 5 elementos
print(busquedaLineal(A,5,3)) #va a imprimir el valor de encontrado
#busquedaLineal(NOMBRE ARREGLO, valor maximo del indice, valor a ENCONTRAR)

