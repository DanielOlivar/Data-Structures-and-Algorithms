#include <stdio.h>		
#include <stdlib.h>
int main() {
	int *dinamico = (int*)malloc(4);     
	int i;					
	* dinamico = 7; 
	*(dinamico + 1) = 8;
	dinamico[2] = 9;			
	*(dinamico + 3) = 10;
	int *dino;
	dino = realloc(dinamico,sizeof(int)*10);   
	for(i = 0; i < 10; i++){
      	dino[i]= (i+1)*10;  					
      	printf("%d  \n",dino[i]);
	}
}

