/*
 * cezar.cpp
 *
 *
 *
 */


#include <iostream>
using namespace std;
void szyfruj(char tekst[], ink klucz) {
    klucz = klucz % 26;
    int i = 0;
    while (tekst[i] != '\0') {
        if((int)tekst[i] + klucz  > 122)
        tekst[i] = (char)((int)tekst[i] + klucz - 26);
        else
            ;
        i++;
    }
}

int main(int argc, char **argv)
{
    char test[100];
    ink kluz = 3;
    cout << "Podaj tekst: " << endl;
    cin >> tekst;
    cout<< "Podaj klucz: " << endl;
    cin >> klucz;
    szyfruj(tekst,klucz);
    cout << tekst;

	return 0;
}

