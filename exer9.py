# #include<stdio.h>
# #include<stdlib.h>
# #include<locale.h>
# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	int idade = 0,cont = 0,totalidade = 0;
# 	float media = 0;
	
# 	for(cont = 1;cont<=2;cont++){
# 		printf("Informe a idade da crian�a: \n");
# 		fflush(stdin);
# 		scanf("%d",&idade);
# 		totalidade = totalidade + idade;
# 	}
	
# 	media = (float)totalidade/2;
# 	printf("\nO total das idades � %d anos \n",totalidade);
# 	printf("\nA m�dia de idade � %.f anos \n",media);
	
# 	system("pause");
# 	return 0;
# }

total = 0

for i in range(2):
    idade = int(input("informe a idade da criança: "))
    total += idade

print("O total das idades: ", total)
print("A media de idade: ", total/2)
