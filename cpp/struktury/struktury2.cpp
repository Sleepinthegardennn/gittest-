/*
 * struktury.cpp
 * 
 * Copyright 2018  <>
 * 
 */


#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

struct osoba {
    char imie[20];
    char nazwisko[20];
    int wiek;
};

void wyswietlDane(osoba o){
    cout << setw(20) << "Imię: " << o.imie << endl;
    cout << setw(20) << "Nazwisko: " << o.nazwisko << endl;
    cout << setw(20) << "Wiek: " << o.wiek << endl;
}

void getOsoby(osoba t[], int ile) {
    for(int i=0; i<ile; i++){
        osoba uczen1;
        cout << "Podaj imię: ";
        cin >> t[i].imie;
        cout << "Podaj nazwisko: ";
        cin >> t[i].nazwisko;
        cout << "Podaj wiek: ";
        cin >> t[i].wiek;
        wyswietlDane(uczen1);
    }
}

void drukujOsoby(osoba t[], int ile) {
    for(int i=0; i<ile; i++){
        osoba uczen1;
        cout << "Podaj imię: ";
        cin >> t[i].imie;
        cout << "Podaj nazwisko: ";
        cin >> t[i].nazwisko;
        cout << "Podaj wiek: ";
        cin >> t[i].wiek;
    }
}

void zapiszDane(osoba t[], int ile){
    ofstream plik("osoby.txt", ios::app);
    if(!plik.is_open()){
        cout << "Błąd otwarcia pliku";
    } else{ 
        for(int i=0; i<ile; i++) {
            cout << t[i].imie << "," << t[i].nazwisko << "," << t[i].wiek << endl;
            plik << t[i].imie << "," << t[i].nazwisko << "," << t[i].wiek << endl;
            }
        }
}


int czytajDane(osoba t[]){
    ifstream plik("osoby.txt");
    string linia;
    int i = 0;
    
    if (plik.is_open()) {
        while(getline(plik, linia)) {
            cout << linia << endl;
            i++;
        }
            
    } else {
        cout << "Błąd otwarcia pliku";
    }
    return i;
}

int main(int argc, char **argv)
{
	//~osoba uczen1;
    //~cout << "Podaj imię: ";
    //~cin >> uczen1.imie;
	//~cout << "Podaj nazwisko: ";
	//~cin >> uczen1.nazwisko;
    //~cout << "Podaj wiek: ";
    //~cin >> uczen1.wiek;
    //~wyswietlDane(uczen1);
    
    int ile;
    cout << "Ile osób? "; cin >> ile;
    osoba tb[ile];
    getOsoby(tb, ile);
    zapiszDane(tb, ile);
    cout << czytajDane(tb) << endl;
    
    return 0;
}

