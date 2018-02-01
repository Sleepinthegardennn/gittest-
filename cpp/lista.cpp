/*
 * lista.cpp
 * 
 */


#include <iostream>
#include "lista.hpp"


Lista::Lista(){
    head = NULL;
    tail = NULL;
}

Lista::~Lista(){
    while(Usun()){;}; 
}

void Lista::Dodaj(int wartosc) {
    ELEMENT *el = new ELEMENT;
    el->wartosc = wartosc;
    el->nast = NULL;
    if(head == NULL) {
        head = el;
        tail = el;
    } else {
        tail->nast = el; //ustawienie wskaznika nast dotychczasowego
        //ostatniegoelementu na adres nowego ostataniego wskaznika
        tail = el; // aktualiz
    }
}

void Lista::Wyswietl() {
    ELEMENT *el = head;
    while (el != NULL){
        std::cout << el->wartosc << " ";
        el = el->nast;
    }
    std::cout << std::endl;
}

bool Lista::Usun(){
    if (head != NULL) {
        if (head == tail){
            delete head;
            head = NULL;
            tail = NULL;
        } else {
            ELEMENT *el = head;
            while(el-> nast !=tail){
                el = el -> nast;
            }
            delete el->nast;
            el->nast=NULL;
            tail = el;
        }
        return true;
    }
    return false;
}

