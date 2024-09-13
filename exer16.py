# #include<stdio.h>
# #include<stdlib.h>
# #include<locale.h>

# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	int idade = 0,conttotal = 0,contIA = 0,contIB = 0,contJA = 0,contJB = 0,contADUL = 0;
	
# 	printf("Qual a idade do nadador? \n");
# 	fflush(stdin);
# 	scanf("%d",&idade);
	
# 	while(idade > 0){
# 		if(idade >=18){
# 			contADUL++;
# 			conttotal++;
# 			printf("ADULTO \n");
# 		}
# 		else{
# 			if(idade >=5 && idade<=7){
# 				contIA++;
# 				conttotal++;
# 				printf("infantil A \n");
# 			}
# 			else{
# 				if(idade>=8 && idade<=10){
# 					contIB++;
# 					conttotal++;
# 					printf("infantil B \n");
# 					}
# 					else{
# 						if(idade>=11 && idade<=13){
# 							contJA++;
# 							conttotal++;
# 							printf("Juvenil A \n");
# 							}
# 							else{
# 								if(idade>=14 && idade<=17){
# 									contJB++;
# 									conttotal++;
# 									printf("Juvenil B \n");
# 								}
# 							}
# 						}
# 					}
# 				}
			
		
	
# 	printf("Qual a idade do nadador? \n");
# 	fflush(stdin);
# 	scanf("%d",&idade);
# }	
# 	printf(" Categoria infantil A sao: %d \n",contIA);
# 	printf(" Categoria infantil B sao: %d \n",contIB);
# 	printf(" Categoria juvenil A sao: %d \n",contJA);
# 	printf(" Categoria juvenil B sao: %d \n",contJB);
# 	printf(" Categoria Adultos sao: %d \n",contADUL);
	
# 	printf("total: %d \n",conttotal);
	
# 	system("pause");
# 	return 0;
# }

cntAdulto = 0
cntIB = 0
cntIA = 0
cntJB = 0
cntJA = 0
cntTotal = 0

idade = int(input('Qual a idade do nadador? '))

while idade != 0:
    if idade >= 18:
        cntAdulto += 1
        print("Adulto")
    else:
        if (idade>=1 and idade <=7):
            cntIA += 1
            print("Infantil A")
        else:
            if (idade>=11 and idade<=13):
                cntIB += 1
                print("Infantil B")
            else:
                if (idade >= 14 and idade <= 17):
                    cntJA += 1
                    print("Juvenil A")
                else:
                    cntJB += 1
                    print("Juvenil B")
    
    idade = int(input("Qual a idade do nadador? "))
    
    cntTotal +=1

print("Categoria infantil A sao: ",cntIA)
print("Categoria infantil B sao: ",cntIB)
print("Categoria juvenil A sao: ",cntJA)
print("Categoria juvenil B sao: ",cntJB)
print("Categoria Adultos sao: ",cntAdulto)

