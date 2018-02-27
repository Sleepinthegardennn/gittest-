#include <iostream>
#include "drzewo.hpp"

using namespace std;

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


int main(int argc, char **argv) {
	cout << "Hello";
	return 0;
}

