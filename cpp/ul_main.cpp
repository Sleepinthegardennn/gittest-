/*
 * ulamek.cpp
 * metoda skracaj :
 * void skracaj() {}
 */



#include <iostream>

using namespace std;

class Ulamek {
private:
    int licznik;
    int mianownik;
public:
    Ulamek(int, int); //deklaracja konstruktora
    void zapisz(int, int);
    void wypisz() {
        cout << licznik << "/" << mianownik;
    }
    
    int get_l() {
        return licznik;
    }
    int get_m() {
        return mianownik;
    }
};
    void skracaj();
    
void Ulamek::skracaj() {
   ; //wykorzystaj algorytm Euklidesa optymalny
}

void Ulamek::zapisz(int l, int m){
    licznik =l;
    if(m !=0) mianownik = m;
    else {
        cout << "Pamietaj nie dziel przez zero";
        exit(1);
    }
    
}

Ulamek::Ulamek(int l, int m){
    licznik =l;
    if(m !=0) mianownik = m;
    else {
        cout << "Pamietaj nie dziel przez zero";
        exit(1);
    }
    
}

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

