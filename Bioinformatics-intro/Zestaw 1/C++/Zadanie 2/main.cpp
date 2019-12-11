#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
float toCelsius(){
	float tempF;
	printf("Podaj temperature w stopniach Farenheita\n");
	scanf("%f", &tempF);
	float tempC = (tempF-32)*5/9;
    printf("%f", tempC);
    return tempC;
}

int main(int argc, char** argv) {
	toCelsius();
	return 0;
}
