#include <iostream>
#include <math.h>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
int prime(int podana){
	int i=2;
	while (i<=sqrt(podana)){
		if(podana%i == 0)return 0;
		else i++;
	}
	return 1;
}


int main(int argc, char** argv) {
	int a;
	for(a=2;a<101;a++){
		if(prime(a))printf("%d\n", a);
}
	return 0;
}
