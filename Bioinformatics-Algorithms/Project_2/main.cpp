#include "pattern_counter_oop.h"

int main(){
    //Testy funkcji
    CountPatterns oric("oriC.txt", "Witaj!");
    oric.drukuj_dna();
    oric.complementary_sequence();
    oric.drukuj_komplementarna();
    oric.pattern_info("AAA");
    oric.most_frequent_patterns_of_given_size(3);
    oric.unique_most_frequent_patterns();
    oric.create_table_from_book();
    oric.oric_finder("CTTGATCAT");
/*Zauwazamy ze w patternach w oriC o dlugosci 9 znajduja siê 2 patterny bedace komplementarne, 
lacznie wystepujac 6 razy w oric*/
    CountPatterns Vibrio("Vibrio.fna");
	//nie drukuje sekwencji oraz jej komplementarnej sekwencji zeby nie zapelniac konsoli
    Vibrio.pattern_info("ATGATCAAG");
    Vibrio.pattern_info("CTTGATCAT");
    Vibrio.pattern_info("TCTTGATCA");
    Vibrio.pattern_info("CTCTTGATC");
    Vibrio.oric_finder("CTTGATCAT");
}
/*Sekwencja ATGATCAAG wystepuje w oriC najczesciej z 9-merow, ponadto wystepuje tam rowniez tyle samo razy sekwencja CTTGATCAT, 
bedaca do niej komplementarna, mozna z tego wywnioskowac iz wybrana sekwencja moze byc nasza szukana, 
sekwencja ta wystepuje w calym genomie 37 razy, ponadto w bliskiej odleglosci w miejscach:
2961525
2961582
2961653
co jest tak bardzo nieprawdopodobne, gdyz mamy az 3 wystapienia na przestrzeni 130 zasad
i do tego w bliskiej odleglosci znajduja sie rowniez 3 wystapienia sekwencji komplementarnej.
Sekwencja komplementarna wystêpuje w podobnym obszarze na pozycjach:
2961542 
2961923 
2962023  
mozemy z tego wywnioskowac ze obszar 2961525 - 2962023 jest obszarem oriC
funkcja szukajaca oric na fragmencie z ksiazki ma wynik porownywalny na calym genomie,
w oric 27-525
w Vibrio 2961525-2962023
mozemy zauwazyc ze:
525-27=498
2962023-2961525=498
co zapewnia ze znaleziony fragment w Vibro to nasz poszukiwany oric*/
