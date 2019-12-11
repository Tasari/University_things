#include "pattern_counter.h"
void pattern_counter(string tekst, string pattern, int &count, vector<int> &positions){
    count = 0;
    for(int i=0;i<tekst.size()-pattern.size()+1;i++){//+1 gdyz nie znajdowalo ostatniej sekwencji
        if(tekst.substr(i, pattern.size()) == pattern){
            count++;
            positions.push_back(i);

        }
    }
}
