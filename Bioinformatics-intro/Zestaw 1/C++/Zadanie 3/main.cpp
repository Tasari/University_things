#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
int silnia (int liczba){
    if (liczba == 0) return 1;
    else return liczba * silnia(liczba - 1);
}


int main(int argc, char** argv) {
	int wartosc;
	int n;
	for(n = 1;n < 11;n++){
  		wartosc = silnia(n);
    	printf("Wynik %d!	| %d\n", n, wartosc);
}
	return 0;
}
