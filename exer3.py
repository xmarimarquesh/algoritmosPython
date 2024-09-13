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

print(10*'-', "TABUADA", 10*'-')

for i in range(10):
    print(i , ' X ', 1, ' = ', i*1)

print(30*'-')

for i in range(10):
    print(i , ' X ', 2, ' = ', i*2)

print(30*'-')

for i in range(10):
    print(i , ' X ', 3, ' = ', i*3)

print(30*'-')

for i in range(10):
    print(i , ' X ', 4, ' = ', i*4)

print(30*'-')

for i in range(10):
    print(i , ' X ', 5, ' = ', i*5)

print(30*'-')

for i in range(10):
    print(i , ' X ', 6, ' = ', i*6)

print(30*'-')

for i in range(10):
    print(i , ' X ', 7, ' = ', i*7)

print(30*'-')

for i in range(10):
    print(i , ' X ', 8, ' = ', i*8)

print(30*'-')

for i in range(10):
    print(i , ' X ', 9, ' = ', i*9)

print(30*'-')

for i in range(10):
    print(i , ' X ', 10, ' = ', i*10)

print(30*'-')