/*
 * tablice.cpp
 * 
 */


#include <iostream>
#include <iomanip>
#include <cstdlib>

using namespace std;


void wypelnij2W(int**tab, int w, int k) {
    srand(time(NULL));
    for(int i=0; i<w; i++){
        for(int j=0; j<k; j++){
            //cout << i << j << endl;
            tab[i][j] = (i+1)*(j+1);
            cout << setw(4) << tab[i][j];
        }
        cout << endl;
    }
    
}
void wprowadzDane(int *t, int ile) { 
    for(int i=0; i <ile; i++) {
        cout << "Podaj liczbę";
        //cin >> tab[i];
        cout << "Adres komórki" << (t + i) << endl;
        cin >> *(t + i);
        
    }
}


int tab1W() {
    int ile = 0;
    cout << "Ile ocen podasz?" << endl;
    cin >> ile;
    
    try{
       int *tab;
       tab = new int[ile];
       wprowadzDane(tab, ile);
       
    } catch(bad_alloc) {
        cout << "Za mało pamieci!";
    return 1;
    }
    return 0;
}

int tab2W(){
    int w, k, i;
    cout << "Ile wierszy i kolumn?";
    cin >> w >> k;
    int **tab;
    
    try{
       tab = new int*[w];
    } catch(bad_alloc) {
        cout << "Za mało pamieci!";
        return 1;
    }
    for(i = 0; i < w; i++) {
        try{
           tab[i] = new int[k];
        } catch(bad_alloc) {
            cout << "Za mało pamieci!";
            return 1;
        }
    }
    wypelnij2W(tab, w, k);
            return 0;
}


int main(int argc, char **argv)
{
    tab2W();
	//tab1W();
	return 0;
}

