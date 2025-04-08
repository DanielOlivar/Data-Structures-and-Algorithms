from time import perf_counter
print("Práctica 13, Becerril Olivar Axel Daniel.")
print("Secuencia de Fibonacci")
inicio = perf_counter()
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def main():
    # Try out the factorial function
    print(" 0! = ", factorial(0))
    print(" 1! = ", factorial(1))
    print(" 2! = ", factorial(2))
    print(" 3! = ", factorial(3))
    print(" 4! = ", factorial(4))
    print(" 5! = ", factorial(5))
    print(" 6! = ", factorial(6))
    print(" 7! = ", factorial(7))
    print(" 8! = ", factorial(8))
    print(" 9! = ", factorial(9))
    print(" 10! = ", factorial(11))
    fin = perf_counter()
    tiempo=fin-inicio
    print("El programa tardó en calcular el factorial: ", tiempo, "segundos.")
main()

inicio2 = perf_counter()
def factorial(n):
    product = 1
    while n:
        product *= n
        n -= 1
    return product

def main():
    # Try out the factorial function
    print(" 0! = ", factorial(0))
    print(" 1! = ", factorial(1))
    print(" 2! = ", factorial(2))
    print(" 3! = ", factorial(3))
    print(" 4! = ", factorial(4))
    print(" 5! = ", factorial(5))
    print(" 6! = ", factorial(6))
    print(" 7! = ", factorial(7))
    print(" 8! = ", factorial(8))
    print(" 9! = ", factorial(9))
    print("10! = ", factorial(10))
    fin2 = perf_counter()
    tiempo2=fin2-inicio2
    print("El programa tardó en calcular el factorial: ", tiempo2, "segundos.")
    
main()
    
    