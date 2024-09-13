# #include <stdio.h>
# #include <stdlib.h>
# #include <locale.h>

# void conta (int x);

# int main(){
	
# 	int num;
	
# 	scanf("%d", &num);
# 	conta(num);
	
# 	system("pause");
# 	return 0;
	
# }

# void conta (int x){
		
# 	if( x > 0) {
# 		printf("%d \n", x);
# 		conta(x - 1);
		
# 	}
# }
	
def recursiva(numero):
    if(numero>0):
        print(numero)
        recursiva(numero-1)

num = int(input(" : "))

recursiva(num)
