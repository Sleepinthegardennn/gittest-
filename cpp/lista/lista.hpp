#ifndef LISTA_HPP
#define LISTA_HPP

struct ELEMENT {
    int wartosc;
    ELEMENT *nastepny;
};

class Lista {
    private: // hermetyzacja
        ELEMENT *head;
        ELEMENT *tail;
        int i;
    public: // interfejs publiczny klasy - API klasy
        Lista(); // konstruktor
        ~Lista(); // dekonstruktor
        void Dodaj(int);
        void Wyswietl();
        bool Usun();
        void Wstaw(int, int);
    
};
#endif
