/*
 * lista_main.cpp
 *
 */


#include <iostream>
#include "lista.hpp"

using namespace std;

int main(int argc, char **argv)
{   
    Lista lista;
    lista.Dodaj(1);    
    lista.Dodaj(2);    
    lista.Dodaj(3);    
    lista.Dodaj(4);    
    lista.Wyswietl();    
    lista.Usun();    
    lista.Wyswietl(); 
    
    return 0;
}

