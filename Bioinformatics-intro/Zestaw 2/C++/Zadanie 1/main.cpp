#include <iostream>
#include <math.h>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
int main(int argc, char** argv) {
	float x1, y1, x2, y2, e;
	printf("Podaj x1:\n");
	scanf("%f", &x1);
	printf("Podaj y1:\n");
	scanf("%f", &y1);
	printf("Podaj x2:\n");
	scanf("%f", &x2);
	printf("Podaj y2:\n");
	scanf("%f", &y2);
	e = sqrt(pow(x1-x2, 2) + pow(y1-y2, 2));
	printf("%f", e);	
	return 0;
}
