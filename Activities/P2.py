from time import perf_counter #Función auxiliar para contar el tiempo
inicio=perf_counter() #Inicio del contador de tiempo
def bubbleSort(C): #Definición de la función
	for i in range(0,len(C)):  #Número de pasadas que dará el programa para acomodarlo
		print("\nPasada",i) #Imprime en que pasada va (1 a 21)
		for j in range(len(C)-1-i):		#Número de comparaciones que hará el programa
			if C[j]>C[j+1]: #Compara si el elemento C[j] es mayor que C[j+1]
				temp = C[j] #Guarda el elemento mayor C[j]
				C[j] = C[j+1] #Ahora C[j] tomará el valor menor comparado anteriormente
				C[j+1] = temp #Ahora C[j+1] tomará el valor mayor
			print(C) #imprime una pasada
A=[10,9,8,7,6,5,4,1,0,2,3]  #Arreglo A de tamaño 11
B=[11,19,18,17,15,16,14,13,12,21,20] #Arreglo B de tamaño 11
C=A+B #Concatenación de los arreglos A y B, para así formar el arreglo C de tamaño 22
bubbleSort(C) #Método de la burbuja
print("\nPor lo tanto la lista C queda de la siguiente manera:")
print(C) #Impresión del arreglo C
fin = perf_counter() #Fin del contador de tiempo
print("\nEl método de la burbuja tardó: ", fin-inicio, " segundos.") #Impresión del tiempo tardado

