from string import ascii_lowercase
from random import choice
from time import perf_counter

def generaPalabra():
    listaPalabras = []
    inicio = perf_counter()
    for j in range (200000):
        palabra = ""
        for i in range (4):
            letra = choice (ascii_lowercase)
            palabra = palabra + letra
        listaPalabras.append(palabra)
    fin = perf_counter()
    print("La lista tardó en generarse: ", fin+inicio, "segundos")
    return listaPalabras
def main():
    lista = generaPalabra()
    miPalabra = input("Teclee una palabra de 4 letras: ")
    encontrada = 0
    for i in range (len(lista)):
        if (miPalabra == lista[i]):
            encontrada = 1
            break
    if encontrada == 0:
        print("No se encontró la palabra ingresada")
    else:
        print("Sí se encontró la palabra ingresada")
main()
            
    