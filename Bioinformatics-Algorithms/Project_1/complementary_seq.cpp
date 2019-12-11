#include "complementary_seq.h"
void complementary_sequence(string starting_sequence, string &complementary_sequence){
    for(int i=starting_sequence.size();i>=0;i--){
        if(int(starting_sequence[i]) == 65){
            complementary_sequence.append("T");
        }
        else if(int(starting_sequence[i]) == 84){
            complementary_sequence.append("A");
        }
        else if(int(starting_sequence[i]) == 67){
            complementary_sequence.append("G");
        }
        else if(int(starting_sequence[i]) == 71){
            complementary_sequence.append("C");
        }
    }
}
