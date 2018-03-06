/*
 * ulamek.cpp
 * metoda skracaj :
 * void skracaj() {}
 */
#include <iostream>
#include "ul_ulamek.h"

using namespace std;

Ulamek::Ulamek(int l, int m){
    licznik =l;
    if(m !=0) mianownik = m;
    else {
        cout << "Pamietaj nie dziel przez zero";
        exit(1);
    }
}

void Ulamek::zapisz(int l, int m){
    licznik =l;
    if(m !=0) mianownik = m;
    else {
        cout << "Pamietaj nie dziel przez zero";
        exit(1);
    }
    
}

void Ulamek::wypisz() {
    cout << licznik << "/" << mianownik;
}
    
int Ulamek::get_l() {
    return licznik;
}

int Ulamek::get_m() {
    return mianownik;
}

void Ulamek::skracaj() {
   ;
}

