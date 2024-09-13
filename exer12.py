# #include<stdio.h>
# #include<stdlib.h>
# #include<locale.h>

# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	int vetmatricula[5], cont = 0, busca = 0;
	
	
# 	for(cont=0; cont<5; cont++){
# 		printf("DIGITE O N�MERO PARA CADASTRO DE MATR�CULA:");
# 		scanf("%d",&vetmatricula[cont]);
	
# 	}
# //  printf("MATR�CULA:%d CADASTRADA\n", vetmatricula[0]);
# //	printf("MATR�CULA:%d CADASTRADA\n", vetmatricula[1]);
# //	printf("MATR�CULA:%d CADASTRADA\n", vetmatricula[2]);
# //	printf("MATR�CULA:%d CADASTRADA\n", vetmatricula[3]);
# //	printf("MATR�CULA:%d CADASTRADA\n\n", vetmatricula[4]);
	
# 	printf("Informe a matr�cula para consulta:");
# 	scanf("%d", &busca);
	
# 	for(cont=0; cont<5; cont++){
		
# 		if(busca == vetmatricula[cont]){
# 			break;
# 		}
# 	}
# 	if(cont == 5){
# 		printf("\n Matricula n�o encontrada \n");
# 	}
# 	else{
# 		printf("Encontrado \n");
# 	}
		
# 	system("pause");
# 	return 0;
# }

matriculas = []

for i in range(5):
    print("Digite o numero da matrícula: ")
    matriculas.append(input())
    print("Matricula ", matriculas[i], "cadastrada! ")

pesquisa = input("Informe a matricula para consulta: ")

for i in range(5):
    if pesquisa == matriculas[i]:
        print("Encontrada")
        achou = True
        break

if(achou != True):
    print("Matrícula não encontrada")