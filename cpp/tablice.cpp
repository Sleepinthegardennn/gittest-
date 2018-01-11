/*
 * tablice.cpp
 * 
 */


#include <iostream>

using namespace std;

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
 
 
int main(int argc, char **argv)
{
	tab1W();
	return 0;
}

