#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
int fibonacci(int arg){
	if(arg<3)return 1;
	else return fibonacci(arg-1)+fibonacci(arg-2);
}
int main(int argc, char** argv) {
	int result, input;
	printf("Podaj ktora liczbe ciagu Fibonacciego chcesz dostac\n");
	scanf("%d", &input);
	result = fibonacci(input);
	printf("Wynik to:%d", result);
	return 0;
}
