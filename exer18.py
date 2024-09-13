# #include<stdio.h>
# #include<stdlib.h>
# #include<locale.h>

# //trabalho pesquisa desordenada;
# //Alunos: Andr� F. P. DIas e Andrey Suprano.

# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	int val[10];
# 	int busca = 0;
# 	int achou = 0;//0 - nao achou, // 1 - achou
# 	int cont;
	
# 	for(cont = 0;cont < 10; cont ++ ){
# 		printf("informe o %d� valor:",cont+1);
# 		fflush(stdin);
# 		scanf("%d",&val[cont]);
# 	}
	
# 	printf("\n Informe um valor pra ser procurado:");
# 	fflush(stdin);
# 	scanf("%d", &busca);
	
		
# 	for(cont = 0;cont < 10; cont ++ ){
# 		if(busca == val[cont]){
# 			achou = achou + 1;
# 		}
# 	}
# 	printf("O n�mero foi achado %d vezes.",achou);
	
	
# system("pause");
# return (0);
# }

val = []
achou = 0

for i in range(10):
    print("Informe o ", i, " valor")
    val.append(int(input()))

busca = int(input("Informe o valor procurado: "))

for i in range(10):
    if(busca == val[i]):
        achou += 1

print("O numero foi achado ", achou, " vezes")
