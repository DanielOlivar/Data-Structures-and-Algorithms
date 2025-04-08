#include "Pila.h"

main(){
    printf("vamos a crear una pila \n");
    Pila miPila = crearPila();
    printf("vamos a ingresar algunos elementos \n");
	meter(&miPila,10);
    meter(&miPila,20);
    meter(&miPila,30);
	meter(&miPila,40);
    meter(&miPila,50);
    printf("El tope de la pila es: %d \n",miPila.tope);    //recuerda que el tope es un índice
	printf("El valor almacenado hasta arriba es: %d \n",miPila.top());    
	int a = sacar(&miPila);
  	printf("Ahora el tope de la pila es : %d \n",top(miPila));
	int b = sacar(&miPila);
  	int c = sacar(&miPila);
  	printf("Ahora el valor hasta arriba es: %d \n",miPila.top());    
	int d = sacar(&miPila);
    printf("valor de c es: %d \n",c);  
	
}


