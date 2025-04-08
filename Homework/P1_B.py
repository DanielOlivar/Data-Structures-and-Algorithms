"""
Created on Sun Mar 14 16:29:20 2021

@author: Gustavo
"""

def valorPi():
    
    print('¿Calcular los numeros de pi?')
    print('1.-SI')
    print('2.-NO')
    
    x=int(input())
    
    if x==1: 
        
        a=int(input("¿Con cuantos numeros quieres calcular pi? "))
        pi=4.0
        
        for i in range(1,a):
            
            if (i+1)%2==0:
                pi=pi-(4/(2*i+1))
                
            else:
                    pi=pi+(4/(2*i+1))        
        print("El valor de pi es: ", pi)
                    
    else:
        print('Hasta luego.!')
        SystemExit
                
valorPi()