/*
 * wskazniki.cpp
 * 
 * 
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int x = 11;
    cout << x << endl;
    cout << &x << endl; //adres zmiennej w pamieci 0x <-- wartosc szesnastkowa
    cout << * &x << endl; //wartosc zmiennej pod adresem
   
    int *px;//definicja wskaznika  do typu całkowietego
    px =&x; //inicjacja wskaznika
    //wskaznik zawsze zawerta adres pamieci 
    cout << px << endl;
    cout << *px << endl;
	
    int y = 100;
    px = &y;
    cout << x << endl;
    cout << &x << endl;
    
    return 0;
}

