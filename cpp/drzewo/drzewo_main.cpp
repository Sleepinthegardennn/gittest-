#include <iostream>
#include "drzewo.hpp"
using namespace std;

int main(int argc, char **argv) {
	
    Drzewo wezel;
    wezel.Dodaj(1);
    wezel.Dodaj(10);
	wezel.Dodaj(8);
	wezel.Dodaj(4);
	wezel.Dodaj(9);
	wezel.Dodaj(20);
	wezel.Dodaj(16);
	wezel.Dodaj(30);
    wezel.WyswietlRosnoco();    
    wezel.WyswietlMalejaco(); 
    
	return 0;
}

