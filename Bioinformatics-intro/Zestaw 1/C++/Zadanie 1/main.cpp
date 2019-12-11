#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {	
    int a;
    while(1){
        printf("Podaj liczbe\n");
        scanf("%d", &a);
        if(a < 1)break;
    }
	return 0;
}
