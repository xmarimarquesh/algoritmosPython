# #include<stdio.h>
# #include<stdlib.h>
# #include<locale.h>
# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
	
# 	media = (n1+n2+n3 )/ 3;
# 	printf("\n");
# 	if (media >= 90){
# 		conceito = 'A';
# 		printf("APROVADO conceito:%c \n COM O ID:%d \n COM AS NOTAS: %.2f %.2f %.2f \n COM A MEDIA: %.2f \n",conceito,id,n1,n2,n3,media);
# 	}
# 	else {
# 		if (media >=75){
# 		conceito = 'B';
# 			printf("APROVADO \n COM O ID:%d \n COM AS NOTAS: %.2f %.2f %.2f \n COM A MEDIA: %.2f \n",id,n1,n2,n3,media);
# 		}
# 		else{
# 			if(media >=60){
# 				conceito = 'C';
# 					printf("APROVADO \n COM O ID:%d \n COM AS NOTAS: %.2f %.2f %.2f \n COM A MEDIA: %.2f \n",id,n1,n2,n3,media);
# 			}
# 			else{
# 				if(media>=40){
# 					conceito = 'D';
# 						printf("REPROVADO \n COM O ID:%d \n COM AS NOTAS: %.2f %.2f %.2f \n COM A MEDIA: %.2f \n",id,n1,n2,n3,media);
# 				}
# 				else{
# 					conceito = 'E';
# 						printf("REPROVADO \n COM O ID:%d \n COM AS NOTAS: %.2f %.2f %.2f \n COM A MEDIA: %.2f \n",id,n1,n2,n3,media);
# 				}
# 			}
# 		}
# 	}
	
# 	system("pause");
# 	return 0;
# }


id_aluno = int(input("Qual numero de identiicação do aluno: "))
notas = []
soma = 0

for i in range(3):
    print("Qual a ", i+1 ,"° nota: ")
    notas.append(int(input()))
    soma += notas[i]

media = soma/3

situacao = ''

if media>=60:
    situacao = 'APROVADO'
else:
    situacao = 'REPROVADO'

print('\n\n >> ',situacao , "\nCOM O ID" , id_aluno , "\nCOM AS NOTAS: " , notas[0] , ' | ' , notas[1]  , ' | ' , notas[1]  , '\nMEDIA: ', media )
    
