#include "iterator.h"
using namespace std;

void iteruj_check(vector<string> iterowalna){
    for(vector<string>::iterator it = iterowalna.begin(); it != iterowalna.end(); ++it){
        cout << distance(iterowalna.begin(), it) << '\t' << *it << endl;
    }
}

void iteruj_i_zloz(vector<string> iterowalna, string &zlozona){
    for(vector<string>::iterator iteracja = iterowalna.begin(); iteracja != iterowalna.end()-1; ++iteracja){//-1 z powodu dublowania sie ostatniej linii
        zlozona.append(*iteracja);
    }
}
