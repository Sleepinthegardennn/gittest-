/*
 * drzewo_bin.cpp
 * 
 * Copyright 2018  <>
 * 
 */

#include <iostream>

using namespace std;

struct Wezel {
    int wartosc;
    Wezel *lewy;
    Wezel *prawy;
} *korzen = NULL; // definicja struktury i utworzenie wskaźnika korzen

Wezel* stworzWezel(int wartosc) {
    Wezel *nowyWezel = new Wezel;
    nowyWezel->wartosc = wartosc;
    nowyWezel->lewy = NULL;
    nowyWezel->prawy = NULL;
    
    return nowyWezel;
}

void dodajWezel(Wezel *wezel, int wartosc) {
    if (korzen == NULL) { // drzewo jest puste!
        korzen = stworzWezel(wartosc); // utworzenie 1. elementu
    } else {
        if (wartosc < wezel->wartosc) { // wstawiamy wartość do lewego poddrzewa
            if(wezel->lewy != NULL) {
                dodajWezel(wezel->lewy, wartosc);  // rekurencyjne wywołanie dodawanie do lewego poddrzewa
            } else {  // lewy potomek nie istnieje
                wezel->lewy = stworzWezel(wartosc);  // tworzymy nowy wezel
            }
        } else { // wstawiamy wartość do prawego poddrzewa
            if(wezel->prawy != NULL) {
                dodajWezel(wezel->prawy, wartosc);  // rekurencyjne wywołanie dodawanie do lewego poddrzewa
            } else {  // prawy potomek nie istnieje
                wezel->prawy = stworzWezel(wartosc);  // tworzymy nowy wezel
            }
        }
    }
}

// funkcja rekurencyjnie przeglądająca drzewo
void wyswietlRosnoco(Wezel *wezel) {
    if (wezel != NULL) { // jeżeli węzeł nie jest pusty
        // rekurencyjnie wyswietl lewo poddrzewo
        wyswietlRosnoco(wezel->lewy);
        // wypisz wartość aktualnego węzła
        cout << wezel->wartosc << ", ";
        // rekurencyjnie wyswietl prawe poddrzewo
        wyswietlRosnoco(wezel->prawy);
    }
}

void wyswietlMalejaco(Wezel *wezel) {
    if (wezel != NULL) { // jeżeli węzeł nie jest pusty
        // rekurencyjnie wyswietl lewo poddrzewo
        wyswietlMalejaco(wezel->prawy);
        // wypisz wartość aktualnego węzła
        cout << wezel->wartosc << ", ";
        // rekurencyjnie wyswietl prawe poddrzewo
        wyswietlMalejaco(wezel->lewy);
    }
}


int main(int argc, char **argv)
{
	dodajWezel(korzen, 10);
	dodajWezel(korzen, 8);
	dodajWezel(korzen, 4);
	dodajWezel(korzen, 9);
	dodajWezel(korzen, 20);
	dodajWezel(korzen, 16);
	dodajWezel(korzen, 30);
    
    cout << "Posortowane drzewo (niemalejąco): ";
    wyswietlRosnoco(korzen);
    cout << "Posortowane drzewo (nierosnaco): ";
    wyswietlMalejaco(korzen);
    
    delete korzen;  // zwolnienie wykorzystywanej pamięci
    
	return 0;
}

