# #include<stdio.h>
# #include<locale.h>

# char par_impar (int p_num);

# void main(){
# 		setlocale(LC_ALL,"Portuguese");
	
# 	char resp;
# 	int num = 0;
	
# 	printf("Informe um N�mero:");
# 	fflush(stdin);
# 	scanf("%d",&num);
	
# 	resp = par_impar(num);
# 	printf("%c\n", resp);
	
# 	system("pause");
# }

# char par_impar (int p_num){
	
# 	char pi;
	
# 	if(p_num % 2 == 0){
# 		pi = 'P';
# 		printf("PAR\n");
# 	}
# 	else{
# 		pi = 'I';
# 		printf("IMPAR\n");
# 	}
	
# 	return pi;
# }

def par_impar(numero):
    if(numero % 2 == 0):
        pi = 'Par'
    else:
        pi = 'Impar'
    
    return pi

num = int(input("Informe um numero: "))
resp = par_impar(num)

print("Resultado:", resp)
