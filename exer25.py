#include<stdio.h>
#include<stdlib.h>
#include<locale.h>
# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	float sal;
	
# 	printf("QUAL O SAL�RIO:");
# 	fflush(stdin);
# 	scanf("%f",&sal);
	
# 	if(sal >5000){
# 		printf("MAIOR QUE R$5.000,00");
# 	}
	
# 	system("pause");
# 	return 0;
# }

salario = float(input("Qual o salario: "))


if(salario >= 5000):
    print("Maior que 5000")