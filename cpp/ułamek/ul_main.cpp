/*
 * ulamek.cpp
 * metoda skracaj :
 * void skracaj() {}
 */



#include <iostream>
#include "ul_ulamek.h"
using namespace std;

int main(int argc, char **argv)
{
	//Ulamek u1, u2;
    Ulamek u1(3, 7);
    Ulamek u2(1, 4);
    //u1.zapisz(3, 8);
    //u2.zapisz(1, 4);
    cout << "Ułamek 1: ";
    u1.wypisz();
    cout << endl <<  "Ułamek 2: ";
    u2.wypisz();
    
    u1.zapisz(7, 9);
    cout << endl << "licznik : " << u1.get_l() << endl;
    cout << "mianownik : " << u1.get_m() << endl;
	
    Ulamek u3(u1.get_l(), u1.get_m());
    u3.wypisz();
    return 0;
}

