#include<stdio.h>
#include<stdlib.h>
# //exercicio 9 aula pr�tica
# int main(){
# 	int code, age;
# 	float height, weight;
	
# 	printf("Qual o codigo:");
# 	 scanf("%d", &code);
# 	printf("Qual o idade:");
#    	 scanf("%d", &age);
# 	printf("Qual o altura:");
# 	 scanf("%f", &height);
# 	printf("Qual o peso:");
# 	 scanf("%f", &weight);
# 	printf("\n");
	
# 	printf("O CODIGO:%d \nA IDADE:%d \nA ALTURA:%.2f \nO PESO:%.2f \n", code, age,height, weight);
	
# 	system("pause");
# 	return 0;	
# }


code = input("Qual o código: ")
age = input("Qual a idade: ")
height = input("Qual a altura: ")
weight = input("Qual o peso: ")

print("O CODIGO " + code + "\nA IDADE " + age + "\nO PESO " + weight + "\nA ALTURA " + height)

