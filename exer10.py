# #include<stdio.h>
# #include<stdlib.h>
# #include<locale.h>

# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
	
# 	int num_tabuada = 0,cont = 0;
	
	
# 	printf("_____________________________________________________\n");
# 	printf("SISTEMA DE TABUADA \n");
# 	printf("_____________________________________________________\n");
# 	printf("digite o n�mero da tabuada que gostaria de consultar: \n");
# 	fflush(stdin);
# 	scanf("%d",&num_tabuada);
# 	printf("%d foi o n�mero digitado.\n",num_tabuada);
	
# 	while(num_tabuada <99){
	
	
# 	switch(num_tabuada){
# 		case 0:
# 			for(cont = 1;cont<=10;cont++){
# 			num_tabuada = 0;
# 			printf("%d X %d = %d \n",0,cont,0*cont);
# 			}
		
# 				break;
		
# 		case 1:
# 			for(cont = 1;cont<=10;cont++){
# 				num_tabuada = 1;
# 				printf("%d X %d = %d \n",1,cont,1*cont);
# 				}
			
			
# 				break;
		
# 		case 2:
# 			for(cont = 1;cont<=10;cont++){
# 				num_tabuada = 2;
# 				printf("%d X %d = %d \n",2,cont,2*cont);
# 				}
			
			
# 				break;
		
# 		case 3:
# 			for(cont = 1;cont<=10;cont++){
# 				num_tabuada = 3;
# 				printf("%d X %d = %d \n",3,cont,3*cont);
# 				}
			
			
# 				break;
		
# 		case 4:
# 			for(cont = 1;cont<=10;cont++){
# 				num_tabuada = 4;
# 				printf("%d X %d = %d \n",4,cont,4*cont);
# 				}
			
			
# 				break;
		
# 		case 5:
# 			for(cont = 1;cont<=10;cont++){
# 				num_tabuada = 5;
# 				printf("%d X %d = %d \n",5,cont,5*cont);
# 				}
			
			
# 				break;
		
# 		case 6:
# 			for(cont = 1;cont<=10;cont++){
# 				num_tabuada = 6;
# 				printf("%d X %d = %d \n",6,cont,6*cont);
# 				}
			
		
# 				break;
		
# 		case 7:
# 				for(cont = 1;cont<=10;cont++){
# 				num_tabuada = 7;
# 				printf("%d X %d = %d \n",7,cont,7*cont);
# 				}
		
# 				break;
		
# 		case 8:
# 			for(cont = 1;cont<=10;cont++){
# 				num_tabuada = 8;
# 				printf("%d X %d = %d \n",8,cont,8*cont);
# 				}
			
			
# 				break;
		
# 		case 9:
# 			for(cont = 1;cont<=10;cont++){
# 				num_tabuada = 9;
# 				printf("%d X %d = %d \n",9,cont,9*cont);
# 				}
			
			
# 				break;
		
# 		case 10:
# 			for(cont = 1;cont<=10;cont++){
# 				num_tabuada = 10;
# 				printf("%d X %d = %d \n",10,cont,10*cont);
# 				}
			
			
# 				break;
		
# 		default:
# 		printf("_____Digite um n�mero de 0 a 10_____ \n\n\n");
# 	}
# 	printf("Digite o n�mero da tabuada que gostaria de consultar, \n");
# 	printf("Ou pressione 99 para sair. \n\n");
# 	fflush(stdin);
# 	scanf("%d",&num_tabuada);
# 	printf("%d foi o n�mero digitado.\n\n\n",num_tabuada);
	
# }
	
# 	system("pause");
# 	return 0;
# }

numero = 1

print('--------- SISTEMA DE TABUADA ---------')

while(numero != 0):
    numero = int(input("\nDigite o numero da tabuada que deseja consultar ou 0 para sair: "))
    
    if numero == 0:
        break
    
    print("\nNUMERO: ", numero)
    
    for i in range(1, 11):
        print(i," X ", numero , " = ", i*numero)
