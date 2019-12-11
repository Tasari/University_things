#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	char input;
	printf("Podaj znak który chcesz sprawdzic\n");
	scanf("%c", &input);
	if(input>='a' && input<='z')printf("Mala litera");
	else if(input>='A' && input <='Z')printf("Duza litera");
	else if(input>='0' && input <='9')printf("Cyfra");
	else printf("Znak specjalny");
	return 0;
}
