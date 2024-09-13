# #include<stdio.h>
# #include<stdlib.h>
# #include<locale.h>
# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	int num = 0,cont = 0;
	
# 	printf("Informe o n�mero: \n");
# 	fflush(stdin);
# 	scanf("%d",&num);
	
# 	for(cont = 1;cont<=num;cont++){
# 		printf("%d \n",cont);
# 	}
	
	
# 	system("pause");
# 	return 0;
# }

numero = int(input("Informe o numero: "))

for i in range(1, numero+1):
    print(i)
