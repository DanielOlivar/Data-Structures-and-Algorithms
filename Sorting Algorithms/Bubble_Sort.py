"""def para definir una función ; nombre en este caso bubbleSort y () 
en este caso A """

def bubbleSort(A):
	for i in range(0,len(A)):  #numero de pasadas, len da la longitud de un arreglo
		print("pasada",i)      #i va de 1 a 4 por los valores del ciclo for
		for j in range(len(A)-1-i):		#comparaciones
			if A[j]>A[j+1]:   
				temp = A[j]
				A[j] = A[j+1]
				A[j+1] = temp
			print(A)
A=[5,4,3,2,1]  #conjunto de datos por lo tanto n=5 y n-1 = 4
bubbleSort(A)
print("\n")
print(A)

     

"""
En python el ciclo for i in range (inicio, fin) es:
para todas las i en el rango de (inicio, fin - 1)

El ciclo for un range nunca tocará el valor final, llegara hasta uno antes.

Cuando el for in range tiene solo un parámetro su inicio es 0

for i in range(1,len(A)): quiere decir que el ciclo for va de i en el 
rango de 1 a longitud de A, que sería 5 """
