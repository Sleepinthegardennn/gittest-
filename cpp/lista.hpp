#ifndef LISTA_HPP
#define LISTA_HPP

struct ELEMENT{
    int wartosc;
    ELEMENT *nast; //wskaznik do nastepnego elementu listy
};

class Lista {
    private: //hermetyzacja danych 
        ELEMENT *head;
        ELEMENT *tail;
    public: //interfejs publiczny (API klasy)
        Lista(); //konstruktor
        ~Lista(); //destruktor
        //memory leaks - wycieki pamieci
      void Dodaj(int);
      void Wyswietl();
      bool Usun();  
         
};

#endif
