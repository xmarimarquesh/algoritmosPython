# #include<stdio.h>
# #include<stdlib.h>
# #include<locale.h>

# //trabalho pesquisa binaria.
# //Alunos: Andr� F. P. DIas e Andrey Suprano.

# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	int vet[10];
# 	int busca = 0;
# 	int cont = 0, medio = 0, alto = 0, baixo = 0;
# 	int achou = 0;
	
# 	for(cont = 0;cont < 10; cont ++ ){
# 		printf("informe o %d� valor:",cont+1);
# 		fflush(stdin);
# 		scanf("%d",&vet[cont]);
# 	}
	
# 	printf("\n Informe um valor pra ser procurado:");
# 	fflush(stdin);
# 	scanf("%d", &busca);
# 	achou = 0;
# 	baixo = 0;
# 	alto = 9;
	
		
# while(baixo <= alto && achou == 0 ){
# 	medio = (baixo + alto )/ 2;
	
# 	if( busca < vet[medio]){
# 		alto = medio + 1;
# 	}
# 	else{
# 		if( busca > vet[medio]){
# 			baixo = medio + 1;
# 		}
# 		else{
# 			achou = 1;
# 		}
# 	}
# }
# if(achou == 1){
# 	printf("FOI ENCONTRADO.");
# }
# 	else{
# 		printf("N�O FOI ENCONTRADO.");
# 	}

# 	system("pause");
# 	return(0);
# }

def ordenar(vetor, tamanho):
    for i in range(tamanho-1):
        for j in range(i+1, tamanho):
            if(vetor[i] > vetor[j]):
                temp = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = temp
    
    return vetor
                
def buscar(vetor, tamanho, busca):
    baixo = 0
    alto = tamanho + 1
    
    while(baixo <= alto):
        medio = int((baixo + alto) / 2)
        
        if(vetor[medio] == busca):
            return medio
        
        elif(vetor[medio] < busca):
            baixo = medio + 1
            
        else:
            alto = medio - 1
    
    return -1

vet = []

for i in range(10):
    print("Informe o ", i+1, " valor: ")
    vet.append(int(input()))

vetor = ordenar(vet, 10)

print("Vetor ordenado: ")
for i in range(10):
    print(vet[i])
    
busca = int(input("Informe o valor a ser pocurado: "))

resultado = buscar(vet, 10, busca)

if(resultado != 1):
    print("O valor ", busca, "foi encontrado na posição ", resultado)
else:
    print("O valor ", busca, " não foi encontrado.")
