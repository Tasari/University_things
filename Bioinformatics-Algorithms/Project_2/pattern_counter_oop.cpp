#include "pattern_counter_oop.h"

CountPatterns::CountPatterns(string nazwa_pliku){//konstruktor z jednym argumentem
    cout << "Uruchamiam Konstruktor" << endl;
	oriC_in.open(nazwa_pliku.c_str());
    if (oriC_in.is_open()) cout << nazwa_pliku << " bedzie analizowany" << endl;
    else {cout << nazwa_pliku << " jest niedostepny. Koncze \n";
    }
    czytany_plik = nazwa_pliku;
    vector<string> linie;
    string jedna_linia;
    while(!oriC_in.eof()){
        oriC_in >> jedna_linia;
        linie.push_back(jedna_linia);
    }
    for(vector<string>::iterator it = linie.begin(); it != linie.end()-1;++it){
        dna.append(*it);
    }
    cout << "Koncze dzialanie konsruktora" << endl << endl;
}

CountPatterns::CountPatterns(string nazwa_pliku, string powitanie){//konstruktor z dwoma argumentami
    cout << "Uruchamiam Konstruktor" << endl;
    oriC_in.open(nazwa_pliku.c_str());
    if (oriC_in.is_open()) cout << nazwa_pliku << " bedzie analizowany" << endl;
    else{cout << nazwa_pliku << " jest niedostepny. Koncze \n";
    }
    czytany_plik = nazwa_pliku;
    vector<string> linie;
    string jedna_linia;
    while(!oriC_in.eof()){
        oriC_in >> jedna_linia;
        linie.push_back(jedna_linia);
    }
    for(vector<string>::iterator it = linie.begin(); it != linie.end()-1;++it){
        dna.append(*it);

    }
    cout << powitanie << endl;
    cout << "Koncze dzialanie konsruktora" << endl << endl;
}

CountPatterns::~CountPatterns(){
    cout << "Koncze dzialanie na pliku "<< czytany_plik << " przy uzyciu destruktora" <<endl;
}

void CountPatterns::drukuj_dna(){
    cout << "Zawartosc pliku: " << czytany_plik << endl;
    cout << dna << endl << endl;
}

void CountPatterns::drukuj_komplementarna(){
    cout << "Nic komplementarna do badanej to:" << endl;
    cout << comp_dna << endl << endl;
}

void CountPatterns::count_pattern(string pattern){
    szukany_pattern = pattern;
    ilosc=0;
    for(int i=0;i<dna.size()-pattern.size()+1;i++){
        if(dna.substr(i, pattern.size()) == pattern){
            ilosc++;
        }
    }
}

void CountPatterns::pattern_positions(string pattern){
    positions.clear();//Czyscimy wektor przy pomocy clear() aby moc ponownie uzyc zmiennej, gdyz positions jest zmienna w calym obiekcie, i jesli tego nie zrobimy to nowe wystapienia dodadza sie do vektora tworzac bledy
    for(int i=0;i<dna.size()-pattern.size()+1;i++){
        if(dna.substr(i, pattern.size()) == pattern){
            positions.push_back(i);
        }
    }
}

void CountPatterns::complementary_sequence(){
    for(int i=dna.size(); i>=0;i--){
        if(int(dna[i]) == 65){
            comp_dna.append("T");
        }
        else if(int(dna[i]) == 84){
            comp_dna.append("A");
        }
        else if(int(dna[i]) == 67){
            comp_dna.append("G");
        }
        else if(int(dna[i]) == 71){
            comp_dna.append("C");
        }
    }
}

void CountPatterns::complementary_pattern(string pattern){
    for(int i=pattern.size(); i>=0;i--){
        if(int(pattern[i]) == 65){
            comp_pat.append("T");
        }
        else if(int(pattern[i]) == 84){
            comp_pat.append("A");
        }
        else if(int(pattern[i]) == 67){
            comp_pat.append("G");
        }
        else if(int(pattern[i]) == 71){
            comp_pat.append("C");
        }
    }
}
void CountPatterns::most_frequent_patterns_of_given_size(int size){
	vector<int> all_counts;
	set<string> set_of_patterns;
	int max_count;
	for(int i=0; i<dna.size()-size+1;++i){
        szukany_pattern = dna.substr(i, size);
        count_pattern(szukany_pattern);//uzycie metody z obiektu w danym obiekcie
        all_counts.push_back(ilosc);
		max_count = *max_element(all_counts.begin(), all_counts.end());
	}
	for(int i=0; i<dna.size()-size;++i){
        if(all_counts[i] == max_count){
           	set_of_patterns.insert(dna.substr(i, size));
			}
    	}
	for(set<string>::iterator ite = set_of_patterns.begin();ite!=set_of_patterns.end();ite++){
		cout <<"Najczestsze sekwencje o dlugosci "<< size << " to: " << *ite << endl << endl;
	}
}
void CountPatterns::unique_most_frequent_patterns(){
    set<string> most_frequent_patterns;//set przetrzymujacy unikalne sekwencje, uzywany do usuniecia duplikatow uzywana tylko lokalnie
    vector<int> all_counts;//zmienna lokalna metody
    int max_count=250;/*poczatkowy max_count zapewniajacy dzialanie algorytmu, kazda liczba > 1 jest dobra
    szuka patternow tak dlugo jak sa jakiekolwiek powtorzenia*/
    for(int kmer=3;;kmer++){//for dziala dopoki nie zostanie uzyta komenda break
        all_counts.clear();//czyszczenie wektora aby ponownie go uzyc po 1 razie
        for(int i=0; i<dna.size()-kmer+1;++i){
            szukany_pattern = dna.substr(i, kmer);
            this->count_pattern(szukany_pattern);//uzycie metody z obiektu w danym obiekcie
            all_counts.push_back(ilosc);
        }
        max_count = *max_element(all_counts.begin(), all_counts.end());//max_element zwraca najwiekszy element w kontenerze
        if(max_count<2){//jezeli nie ma wiecej powtorzen, konczy petle
            break;//konczy dzialanie petli
        }
        else{
            for(int i=0; i<dna.size()-kmer;++i){
                if(all_counts[i] == max_count){
                    pair<set<string>::iterator,bool> check = most_frequent_patterns.insert(dna.substr(i, kmer));
                    /*insert zwraca kontener z dwoma roznymi typami zmiennych,
                    pierwsza to miejsce w kontenerze w ktory wkladamy zmienna, 
                    a druga to zmienna boolowska, ktora == True jezeli wlozenie sie udalo, 
                    lub False jezeli instrukcji nie udalo sie wlozyc zmiennej do kontenera,
                    uzywam jej tu zeby sprawdzic czy w secie jest juz dana zmienna, jezeli jest,
                    to instrukcja zwraca False*/
                    if(check.second){//wyciaga drugi element z pair, i jezeli == False to nie wklada substringa do vectora, gdyz ten sie tam znajduje
                        unique_ordered_most_frequent_patterns.push_back(dna.substr(i,kmer));
                    } 
                }
            }
        }
    }
}

void CountPatterns::complete_pattern_print(){
    cout << "Sekwencja " << szukany_pattern <<" o dlugosci " <<szukany_pattern.size() << " wystepuje " << ilosc << " razy w miejscach: ";
        for(vector<int>::iterator itera = positions.begin();itera!= positions.end();itera++){
            cout << *itera  <<" ";
    }
    cout << endl << endl;
}

void CountPatterns::create_table_from_book(){
    for(vector<string>::iterator ite = unique_ordered_most_frequent_patterns.begin();ite!=unique_ordered_most_frequent_patterns.end();ite++){
        count_pattern(*ite);
        pattern_positions(*ite);
        complete_pattern_print();
    }
    cout << "Nie ma wiecej powtarzajacych sie patternow" <<endl << endl;
}

void CountPatterns::pattern_info(string pattern){
    count_pattern(pattern);
    pattern_positions(pattern);
    complete_pattern_print();
}

void CountPatterns::distance_finder(string pattern){
    pattern_positions(pattern);
    int pierwsze=-1;
    int drugie=-1;
    int trzecie=-1;
    for(vector<int>::iterator iterat = positions.begin();iterat != positions.end();iterat++){
        if(trzecie == -1){
            trzecie = *iterat;
            continue;//continue powoduje pominiecie dalszych instrukcji i rozpoczecie kolejnej iteracji petli
        }
        if(drugie == -1){
            drugie = trzecie;
            trzecie = *iterat;
            continue;
        }
        pierwsze = drugie;
        drugie = trzecie;
        trzecie = *iterat;
        if(drugie-pierwsze < 500){
            if(trzecie-drugie < 500){
                if(trzecie-pierwsze < 500){//zapewnia dystans maksymalny na ktorym sekwencja wystepuje 3 razy
                    all_posit_for_oric.push_back(pierwsze);
                    all_posit_for_oric.push_back(drugie);
                    all_posit_for_oric.push_back(trzecie);
                }              
            }
        }
    }
}

void CountPatterns::oric_finder(string pattern){
    distance_finder(pattern);
    complementary_pattern(pattern);
    distance_finder(comp_pat);
    cout << "Miejsce OriC zostalo znalezione w miejscach: " << *min_element(all_posit_for_oric.begin(), all_posit_for_oric.end()) <<"-"<<*max_element(all_posit_for_oric.begin(), all_posit_for_oric.end()) << endl;
}
