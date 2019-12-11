#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	int number, reversed = 0;
	printf("Podaj liczbe aby pokazac ja w odwrotnej kolejnosci\n");
	scanf("%d", &number);
	while(number>0){
		reversed = reversed*10 + number%10;
		number = number/10;
	}
	printf("Twoja liczba w odwrotnej kolejnosci: %d", reversed);
	return 0;
}
