#include<stdio.h>
#include<stdlib.h>
#include<locale.h>
# int main(){
# 	setlocale(LC_ALL,"Portuguese");
	
# 	int num = 0,cont = 0;
	
# 	printf("_____________________tabuada do 7________________________________\n");
# 	for(cont = 1;cont<=10;cont++){
# 		num = 7;
# 		printf("%d X %d = %d \n",7,cont,7*cont);
# 	}
# 	printf("_____________________tabuada do 8________________________________\n");
# 	for(cont = 1;cont<=10;cont++){
# 		num = 8;
# 		printf("%d X %d = %d \n",8,cont,8*cont);
# 	}
	
# 	system("pause");
# 	return 0;
# }

print(10*'-', "TABUADA", 10*'-', '\n')


for i in range(1, 11):
    print("( ",i, " )")
    for j in range(1, 11):
        
        print(i , ' X ', j, ' = ', i*j)
        
    print(30*'-')

