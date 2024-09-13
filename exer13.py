# #include<stdio.h>
# #include<stdlib.h>
# #include<locale.h>

# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	int num[5];
	
# 	num[0] = 10;
# 	num[1] = 20;
# 	num[2] = 30;
# 	num[3] = 40;
# 	num[4] = 50;
	
# 	printf("%d\n", num[0]*0);
# 	printf("%d\n", num[1]*1);
# 	printf("%d\n", num[2]*2);
# 	printf("%d\n", num[3]*3);
# 	printf("%d\n", num[4]*4);
	
# 	system("pause");
# 	return 0;
# }

numero = [10, 20, 30, 40, 50]

for i in range(len(numero)):
    print(numero[i])