# #include <stdio.h>
# #include <stdlib.h>
# #include <locale.h>

# int FAT(int x);

# int main (){
# 	 setlocale(LC_ALL,"Portuguese");
	 
# 	 int num, fatorial;
	 
# 	 scanf("%d", &num);
# 	 fatorial = FAT(num);
	 
# 	 printf("\n O fatorial de %d �: %d\n\n\n", num, fatorial);
	 
# 	 system("pause");
# 	 return 0;
# }

# int FAT (int p_num){
	
# 	if(p_num == 0){
		
# 		return 1;
# 	}
# 	else{
# 		printf("%d � um dos n�meros.\n",p_num);
# 		return p_num * FAT(p_num - 1);
# 	}
# }

def recursiva(numero):
    if numero == 0:
        return 1
    else:
        print(numero, "é um dos numeros ")
        return numero * recursiva(numero-1)
    
num = int(input(" : "))

fatorial = recursiva(num)

print("O fatorial de ", num, " é ", fatorial)