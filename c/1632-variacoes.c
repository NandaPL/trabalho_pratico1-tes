#include <stdio.h>
#include <stdlib.h>
#include <string.h> //Jeniffer Macena 
#include <math.h>

//variacao que os caracteres poderao ter na senha
char senhaEspecial[15] = {'a', 'A', '4', 'E', 'e', '3', 'i', 'I', '1', 'o', 'O', '0', 's', 'S', '5'};

//Funcao para verificar se caractere contem um tipo especial na senha
int caractereEspeciais(char caractere){
  int i;  
  for(i=0; i<15; i++){
  	if(caractere == senhaEspecial[i])
      return 1;
  }
  return 0;
}

int main(){

  char senha[18];
  int t, i, j, cont;

  scanf("%i", &t); // casos de teste
  for(cont = 0; cont < t; cont++){
	scanf("%s", senha); //senha do usuario amigo
	for(i=0, j=1; senha[i] >= 32; i++)
	    if(caractereEspeciais(senha[i])) // utiliza a funcao para verificar a senha do amigo, ou seja 
	    	j *= 3;						//se tem em alguma posicao algum caractere especial, se sim sua variacao sera ate 3
	    else
	    	j *= 2;						//Senao, a variacao sera de apenas 2 caracteres
	    printf("%d\n", j);	// ao final, sera imprimido o valor calculado
	}
	
  return 0;
}