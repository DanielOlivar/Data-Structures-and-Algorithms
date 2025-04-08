#include <stdio.h>

void main() {
    int tam = obtenerCantidad();
    int* arraydin = calloc(tam,sizeof(int));
    leer(tam, arraydin);
    imprimir(tam, arraydin);
    free(*arraydin);
}
int obtenerCantidad() {
    int cantidad;
    printf("Cuántos numeros va a ingresar ?: ");
    scanf("%i", &cantidad);
    return cantidad;
}
void leer(int size, int* array) {
    for (int i=0;i < size; i++) {
        printf("ingrese el elemento \n");
		scanf("%i", &array[i]);
    }
}
void imprimir(int size, int* pepe) {
    for (int i=0 ;i < size; i++) {
        printf("%i ", pepe[i]);
    }
}

