"""
Created on Sun Mar 14 16:11:59 2021

@author: Gustavo
"""

import math

def ResEc():
    
    print("quieres resolver una ecuacion de segundo grado?")
    print('1.- SI')
    print('2.- NO')
    b=int(input())

    while b == 1:
        a=float(input("Ingresa el término cuadrático a: "))
        b=float(input("Ingresa el término lineal b: "))
        c=float(input("Ingresa el término independiente c: "))
        d = b*b-4*a*c
        
        if d>0:
            r1=(-b+math.sqrt(d))/(2*a)
            r2=(-b-math.sqrt(d))/(2*a)
            print("Tus raíces son ",r1," y ",r2)
            
        elif d==0:
            r1=(-b/(2*a))
            print("Solo hay una raíz real ",r1)
        
        else:
            print("No hay raíces reales ni complejas")
            
            
ResEc()