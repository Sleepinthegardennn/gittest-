#!/usr/bin/env python
# -*- coding: utf-8 -*-

def osoba(imie, nazwisko, wiek):
    return {'imie': imie, 'nazwisko': nazwisko, 'wiek': wiek}


def pobierzDane(ile):
    lista = []
    for i in range(0, int(ile)):
        imie = input('POdaj imię: ')
        nazwisko = input('POdaj nazwisko: ')
        wiek = input('POdaj wiek: ')
        lista.append(osoba(imie, nazwisko, wiek))
    return lista


def wyswietlDane(lista):
    for slow in lista:
        print('Imie: ', slow['imie'])
        print('Nazwisko: ', slow['nazwisko'])
        print('Wiek: ', slow['wiek'])


def zapiszDane(lista):
    with open ('osoby.txt', 'w')as plik:
        for slow in lista:
            plik.write(','.join(slow.values()) + '\n')


def main(args):

#   osoba1 = osoba1('Adam', 'Ktoś', 23)
#   print(osoba1.keys())
#   peint(osoba1.values1())
#   print(osoba1['nazwisko'])
    ile = input('Ile osob wprowadzisz?')
    lista = pobierzDane(ile)
    print(lista)
    wyswietlDane(lista)
    zapiszDane(lista)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
