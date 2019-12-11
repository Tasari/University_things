#include "czytaj_plik.h"
#include "pattern_counter.h"
#include "frequent_patterns.h"
#include "iterator.h"
#include "complementary_seq.h"

int main(){
    string plik("oriC.txt");
    vector<string> genom;
    
    cout << "Program oriC" << endl;
    cout << "Uruchamiam plik " << plik << endl;

//Odczytanie pliku
    czytaj_plik(plik, genom);
    string sekwencja;
//Zlozenie pliku
    iteruj_i_zloz(genom, sekwencja);
    cout << "Jego sekwencja to:" << endl << sekwencja << endl << endl;

//test funkcji liczacej i pokazujacej pozycje podanego patternu
    int count;
    vector<int> positions;
    pattern_counter(sekwencja, "AAA", count, positions);
    cout << "Wybrana sekwencja wystapila " << count << " razy, zaczynajac sie w miejscach o indeksach:" << endl;
    for (vector<int>::iterator index = positions.begin(); index != positions.end(); ++index){
        cout << *index << endl;
    }
    cout << endl;
//test funkcji tworzacej sekwencje komplementarna
    string sekwencja_komplementarna;
    complementary_sequence(sekwencja, sekwencja_komplementarna);
    cout << sekwencja_komplementarna << endl << "^ sekwencja komplementarna" << endl << endl;
//test funkcji tworzacej set najczestszych wystepujacych patternow (W instrukcjach na "OK" bylo podane tylko najczesciej wystepujace
//bez podawania poczatku czy ilosci patternow)
    set<string> frequent_patterns_list;
    for (int i=3;i<10;i++){
        frequent_patterns(sekwencja, i, frequent_patterns_list);
    }    
    cout << "Najczesciej wystepujace patterny w zakresie dlugosci 3-9 to:" << endl;
    for (set<string>::iterator ite = frequent_patterns_list.begin(); ite != frequent_patterns_list.end(); ++ite){ 
        cout << *ite << endl;
    }
  /***************************************************************************************************************/
 /*******************************************Dzialanie na pliku FASTA********************************************/ 
/***************************************************************************************************************/ 
    cout << endl << endl;
	string vibrio("Vibrio.fna");//zapisanie nazwy pliku w zmiennej
    vector<string> vibrio_all_lines; //inicjacja wektora z liniami z pliku
    string vibrio_all; //inicjacja stringa gdzie trzymany bedzie kod genetyczny
    czytaj_plik(vibrio, vibrio_all_lines);//Otworzenie pliku i wpisanie linii do wektora
    iteruj_i_zloz(vibrio_all_lines, vibrio_all);//Zlozenie wektora w string
    int count_vibrio;//zainicjowanie zmiennej w ktorej trzymana bedzie ilosc wystapien sekwencji w genomie
    vector<int> positions_vibrio;//vektor pozycji w ktorych znalezlismy sekwencje
    pattern_counter(vibrio_all, "ATGATCAAG", count_vibrio, positions_vibrio);//liczenie wystapien patternow
    cout << "Liczba sekwencji w genomie: "<< count_vibrio << endl <<"Na pozycjach:" << endl;
	for (vector<int>::iterator index_vibrio = positions_vibrio.begin(); index_vibrio != positions_vibrio.end(); ++index_vibrio){///przeiterowanie przez vektor
    cout << *index_vibrio << endl;//wypisywanie pozycji i ilosci wystapien
}
/*Sekwencja ATGATCAAG wystepuje w oriC najczesciej z 9-merow, ponadto wystepuje tam rowniez tyle samo razy sekwencja CTTGATCAT, 
bedaca do niej komplementarna,mozna z tego wywnioskowac iz wybrana sekwencja moze byc nasza szukana, 
sekwencja ta wystepuje rowniez w calym genomie 37 razy, ponadto w bliskiej odleglosci w miejscach:
2961525
2961582
2961653
co jest bardzo nieprawdopodobne, gdyz mamy az 3 wystapienia na przestrzeni 130 zasad, 
kolejna roznica pomiedzy najblizszymi wystapieniami tej sekwencji jest bliska 3 000 zasad, 
mozemy z tego wywnioskowac ze obszar bliski 2961525 - 2961653 jest obszarem oriC, 
a sekwencja ATGATCAAG prawdopodobnie jest DnaA-boxem.
*/
    return 0;
    
}
