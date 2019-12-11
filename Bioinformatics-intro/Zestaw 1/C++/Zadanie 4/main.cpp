#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	int number;
	int sum = 0;
	int x;
	printf("Podaj liczbe ktorej sume cyfr chcesz obliczyc\n");
	scanf("%d", &number);
	while(number>0){
		x = number%10;
		sum = sum+x;
		number = number/10;
	}
	printf("%d", sum);
	return 0;
}
