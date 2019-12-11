#include "czytaj_plik.h"
void czytaj_plik(string nazwa_pliku, vector<string> &genom){
    
    ifstream plik_czytany(nazwa_pliku.c_str());

    if (plik_czytany.is_open()){
        cout << nazwa_pliku << " jest dostepny do analizy" << endl;
    }
    else {
        cout << nazwa_pliku << " jest niedostepny";
        exit(0);
    }

    string jedna_linia;
    while ( !plik_czytany.eof()) {
        plik_czytany >> jedna_linia; 
        genom.push_back(jedna_linia);
    }
return;
}
