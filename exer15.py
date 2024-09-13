# #include<stdio.h>
# #include<stdlib.h>
# #include<locale.h>

# int main(){
# 	setlocale(LC_ALL,"Portuguese");

# 	int mat1[4][4];
# 	int l,c;
# 	int valor = 1;
# 	int soma = 0;
	
# 	for(l = 0; l < 4; l++){
# 		for(c = 0; c < 4; c++){
# 		mat1[l][c] = valor;
# 		valor = valor * 2;

# 		soma = soma + mat1[l][c];
# 		}
# 	}
	
# 	for(l = 0; l < 4; l++){
# 		for(c = 0; c < 4; c++){
# 			printf("| %d |",mat1[l][c]);
# 		}
# 		printf("\n");
# 	}
	
# 	printf("A soma da matriz = %d\n\n",soma);
	
# system("pause");
# return 0;
# }

matriz = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ]

valor = 1
soma = 0

for i in range(4):
    for j in range(4):
        matriz[i][j] = valor
        valor *= 2
        soma += matriz[i][j]

for i in range(4):
    for j in range(4):
        print(matriz[i][j])
        
print("Soma da matriz:", soma)
