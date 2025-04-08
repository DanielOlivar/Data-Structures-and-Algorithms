# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 17:14:44 2021

@author: Gustavo
"""

def ciclos():
    num = int (input("Introduce un numero entero positivo: "))
    
    for i in range(num + 1):
        print("* "*i)

    print(" ");

    cont = 0
    while cont < num:
        cont = cont + 1
        print("* "*num)
   
    
ciclos()