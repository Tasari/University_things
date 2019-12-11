#include<iostream>
#include<fstream>
#include<vector>
#include<set>//biblioteka z setem, set nie przyjmuje duplikatów gdyz przyjmuje wartosci jako klucze, a klucze musza byc unikalne
#include<algorithm>//biblioteka z max i min element

using namespace std;

class CountPatterns{
//domyslnie wszystko jest prywatne
    string dna;//badany lancuch
    string comp_dna;//lancuch komplementarny do badanego
    fstream oriC_in;//strumien otwierajacy plik
    string czytany_plik;//pamieta nazwe pliku
    string szukany_pattern;//pamieta ostatni poszukiwany pattern w pattern counter
    int ilosc;//Pamieta ilosc wystapien ostatniego patternu uzytego w pattern counter
    vector<int> positions;//Pamieta miejsca wystapien ostatniego patternu z pattern positions
    vector<string> unique_ordered_most_frequent_patterns;//vector w ktorym kolejnosc znalezienia jest zachowana 
    string comp_pat;//Sekwencja komplementarna potrzebna do wyszukania oric
    vector<int> all_posit_for_oric;//Tabela przetrzmujaca bliskie wystapienia patternu, oraz patternu do niego komplementarnego
    
    void count_pattern(string pattern); //metoda zliczajaca wystapienia lacucha, pobiera string jakiego ma szukac, zapisuje pattern w szukany_pattern i ilosc wystapien w ilosc
    void pattern_positions(string pattern);//metoda zliczajaca pozycje lancucha, pobiera string jakiego ma szukac, zapisuje pozycje w wektorze positions
    void complementary_pattern(string pattern);//metoda tworzaca lancuch komplementarny do lancucha z pliku, tworzy pattern komplementarny do podanego, uzywany do poszukiwan oric zapisywany w comp_pat
    void distance_finder(string pattern);//Metoda znajdujaca miejsca w ktorych na przestrzeni 500 zasad znajduja sie 3 wystapienia patternu, zapisuje je wszystkie w wektorze all_posit_for_oric
    void complete_pattern_print();//Metoda wypisujaca miejsca w "tabelkowej" wersji
    
	public:
        CountPatterns(string plik_do_czytania);//nazwa pliku w konstruktorze, laduje podany plik do programu
        CountPatterns(string plik_do_czytania, string powitanie);//nazwa pliku w konstruktorze, laduje podany plik do programu, i drukuje powitanie (Nie mialem innego pomyslu na przeladowany konstruktor :))
        void drukuj_dna(); //pokazuje zawartosc lancucha badanego
        void drukuj_komplementarna();//pokazuje zawartosc lancucha komplementarnego
        void complementary_sequence();//metoda tworzaca lancuch komplementarny do lancucha z pliku zapisuje go w comp_dna
        void unique_most_frequent_patterns();//metoda tworzaca vector z najczestrzymi patternami ustawionymi w kolejnosci znajdowania, zapisuje wynik w unique_ordered_most_frequent_patterns
        void create_table_from_book();//Metoda tworzaca tabelke z ksiazki
        void oric_finder(string pattern);//Metoda znajdujaca miejsce oric i wypisujaca je
        void pattern_info(string pattern);//Metoda publiczna ktora zbiera informacje na temat patternu, ilosc oraz pozycje oraz je wypisuje
        void most_frequent_patterns_of_given_size(int size);//Szuka najczestrzego patternu o danej wielkosci jak podano w "OK za 2 projekt"
        ~CountPatterns();//Destruktor wyswietlajacy komunikat



};
