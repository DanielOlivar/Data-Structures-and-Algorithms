inicio=1 #Valor inicial del ciclo while
primo=0 #Valor inicial de los numeros primos
par=0 #Valor inicial de los numeros pares
while(inicio<301): #Compara que sean numeros menores a 301
    num=inicio #Asignación de un numero
    div=2 #Valor entre el que se dividira num
    while num>div: #Compara que num sea mayor que 2 
        if num % div == 0: #Determina si NO es primo
            break
        elif num % div != 0: #Aumetna el valor de div para ver si Es primo
            div=div+1 
        if num == div: #Determina si ES primo
           print(num,"primo.")
           primo=primo+1 #Contabiliza los numeros primos
    inicio=inicio+1 #Aumenta el numero
    if num%2 == 0: #Determina si es par
        print(num,"par")
        par=par+1 #Contabiliza los numeros pares
print("Se generaron correctamente numeros del 1 al 300.")
print("En total hay ",primo, "números primos y ", par, "números pares")
        