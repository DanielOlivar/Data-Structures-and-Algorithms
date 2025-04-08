# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 17:57:06 2021

@author: Vianey Alcantar
"""
def Cifravolteada(x):
    print("Cifra sin modificar:\n", Y)
    cifra1=  Y%10
    cifra2=  int ((Y%100)/10)
    cifra3=  int ((Y%1000)/100)


    print("Cifra modificada\n", str(cifra1)+str(cifra2)+str(cifra3))



Y= int(input("Ingrese una cifra:\n"))
Cifravolteada(Y)