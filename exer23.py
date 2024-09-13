# #include <stdio.h>
# #include <stdlib.h>
# #include <locale.h>

# int N(int p_num);

# int main(){
# 	setlocale(LC_ALL,"Portuguese");
# 	int num, resp = 0;
	
# 	printf("INFORME UM NUMERO INTEIRO POSITIVO:");
# 	fflush(stdin);
# 	scanf("%d", &num);
	
# 	resp = N(num);
	
# 	printf("%d � o somat�rio dos numeros.", resp);
	
# 	system("pause");
# 	return 0;
# }

# int N(int p_num){
	
# 	int acumulo = 0;
	
# 	if(p_num > 0){

# 	printf("%d � um dos n�meros.\n",p_num);
	
# 	acumulo = 	N(p_num - 1) + p_num;
	
# 	}
	
# 	return acumulo;
	
# }

def recursiva(numero):
    acumulo = 0
    
    if(numero > 0):
        print(numero,"é um dos números ")
        acumulo = recursiva(numero-1)+numero
        
    return acumulo

num = int(input(" : "))

soma = recursiva(num)

print("Somatório dos numeros: ", soma)
