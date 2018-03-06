/*
 * ulamek.cpp
 * metoda skracaj :
 * void skracaj() {}
 */
#ifndef ULAMEK_H
#define ULAMEK_H

class Ulamek {
private:
    int licznik;
    int mianownik;
public:
    Ulamek(int, int); 
    void zapisz(int, int);
    void wypisz();
    int get_l();
    int get_m();
    void skracaj();
};
#endif
