#include "frequent_patterns.h"

void frequent_patterns(string text, int k_mer, set<string> &frequent_patterns){
    vector<int> all_counts;
    int max_count;
    for(int i=0; i<text.size()-k_mer+1;++i){
        int counted = 0;
        vector<int> posit;
        string pattern = text.substr(i, k_mer);
        pattern_counter(text, pattern, counted, posit);
        all_counts.push_back(counted);
    }
    max_count = *max_element(all_counts.begin(), all_counts.end());//max_element zwraca najwiekszy element w kontenerze
    for(int i=0; i<text.size()-k_mer;++i){
        if(all_counts[i] == max_count){
            frequent_patterns.insert(text.substr(i, k_mer));
        }
    }

}
