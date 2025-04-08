def crearSubArreglo(A, indIzq, indDer): #[], p y q 
	 return A[indIzq:indDer+1] #Operaciones para sacar pedazos de un arreglo, slice
def Merge(A,p,q,r):
	Izq = crearSubArreglo(A,p,q)
	Der = crearSubArreglo(A,q+1,r)
	i=0
	j=0
	for k in range(p,r+1):
		if(j>=len(Der)) or (i < len(Izq) and Izq[i] < Der[j]): #Hace la mezcla
			A[k]=Izq[i] #
			print("lista Izquierda",Izq)
			i=i+1
		else:
			A[k]=Der[j]
			print("lista derecha",Der)
			j=j+1
def MergeSort(A,p,r):  #A arreglo, P primer idnice del arreglo, R ultimo indice arreglo
	if r - p > 0: #Verifica que tenga más de un elemento, si solo es uno, ya estaría acomodado
		q = int((p+r)/2) #divide virtualmente entre 2 el arreglo
		MergeSort(A,p,q) #Pasa el arreglo y los indices 0 y el resultado de q
		MergeSort(A,q+1,r) #
		Merge(A,p,q,r) #
A=[5,4,3,2,1,0]
MergeSort(A,0,5)  #A arreglo, primer indice, ultimo indice del arreglo
print(A)

"""A=[5,4,3,2,1,0]
MergeSort(A,0,5)
A=[10,7,3,1]
MergeSort(A,0,3)"""