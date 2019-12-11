#include "pattern_counter.h"
#include <algorithm> //biblioteka zawierajaca max_element, zwracajacy najwiekszy element z kontenera
#include <set> //biblioteka dolaczajaca set, kontener ktory zapobiega powtorzeniom, jest to kontener sortujacy automatycznie elementy 
//alfabetycznie, uzywa kluczy jako elementow, a jako iz kontener nie moze miec 2 takich samych kluczy to zapobiega on duplikatom

using namespace std;
//Funkcja ktora korzystajac z funkcji pattern_counter okresla najczesciej wystepujace patterny.
//podajemy sekwencje w ktorej szukamy patternow, dlugosc szukanego patternu, oraz set gdzie maja zostac zapisane patterny znalezione
void frequent_patterns(string, int, set<string> &);
