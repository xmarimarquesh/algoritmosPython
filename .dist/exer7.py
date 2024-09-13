# #include<stdio.h>
# #include<stdlib.h>
# #include<locale.h>
# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	float sal, total, media;
# 	int cont;
	
# 	for(cont = 1; cont<=5; cont++){
# 		printf("Informe o salario do funcionario %d:",cont);
# 		scanf("%f", &sal);
# 		total = total + sal;
# 	}
# 	printf("Total: %.2f \n",total);
# 	media = total / (cont-1);
# 	printf("Media: %.2f \n",media);
	
# 	system("pause");
# 	return 0;
# }

salario = []
soma = 0

for i in range(5):
    print("Informe o salario do funcionario", i+1)
    salario.append(float(input()))
    soma += salario[i]

print("Total: ", soma)
print("Media: ", soma/5)
