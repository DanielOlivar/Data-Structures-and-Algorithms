"""---------------------Tiempo de ejecucion con timeit---------------------"""

from timeit import default_timer

'Funcion que calcula la serie de Fibonacci'
def fibonacci(a):
        if a==1 or a==2:
            return 1
        return fibonacci(a-1) + fibonacci(a-2)
inicio=default_timer()
print("El quinto elemento de la serie del Fibonacci es: " + str(fibonacci(5)))
fin=default_timer()

'Imprime y calcula el tiempo de ejecucion de fibonacci'
print("Tiempo de ejcucion es: " + str(fin - inicio))

"""-----------------------Tiempo de ejecucion con time---------------------"""

"""
import time

'Funcion que calcula la serie de Fibonacci'
def fibonacci(a):
        if a==0 or a==1:
            return 1
        return fibonacci(a-1) + fibonacci(a-2)

inicio = time.time()
time.sleep(1)
print("El quinto elemento de la serie del Fibonacci es: " + str(fibonacci(5)))
fin = time.time()

'Imprime y calcula el tiempo de ejecucion de fibonacci'
print("Tiempo de ejecucion: ", fin-inicio) 
"""

