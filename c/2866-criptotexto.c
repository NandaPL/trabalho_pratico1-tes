#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main (){
	//declaro as variaveis
	char palavra[101], saida[101];
	unsigned short casos, i, j, tamanho;
	//entrada de numeros de casos
	scanf("%hu", &casos);

	while (casos--){
		scanf(" %s", palavra);
		//determinando o tamanho da string
		tamanho = strlen(palavra);

		i = tamanho - 1;
		j = 0;

		// Leio a string de tras para frente visando pegar os caracteres na ordem certa e coloca-los na string de saida;
		
		while (tamanho--){
			// O padrao da questao sao os caracteres minusculos, lidos de tras para frente, formam uma palavra;
			
			if (islower(palavra[i])){
        saida[j++] = palavra[i--];
      }	else{
        i--;
      }
				
		}

		saida[j] = '\0';
		//printar saida
		printf("%s\n", saida);
	}
}