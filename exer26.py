#include<stdio.h>
#include<stdlib.h>
#include<locale.h>
# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	int num;
	
# 	printf("INFORME UM N�MERO:");
# 	fflush(stdin);
# 	scanf("%d",&num);
	
# 	if(num % 2 == 0){
# 		printf("Este � um n�mero par.\n");
# 	}
# 	else{
# 		printf("Este � um n�mero �mpar.\n");
# 	}
		
# 	system("pause");
# 	return 0;
# }


numero = int(input("Informe um numero: "))

if(numero%2 == 0):
    print("Esse é um numero par")
else:
    print("Esse é um número ímpar")

