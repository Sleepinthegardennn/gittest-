#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dane.py
import csv 

def dane_z_pliku(plik, delimiter='\t'): #delimiter='\t' - inne dane
    dane = []
    with open(plik,'r') as plikcsv: # wszystkie operacje wciete. bez zamykania.'r' do pdczytu. uchwyt do pliku
        tresc = csv.reader(plikcsv, delimiter=delimiter) #dane #csv.reader dane sa oddzielone jednym znakiem        
        for rekord in tresc:
            dane.append(rekord)
    return dane
    
def wyczysc_dane(dane, pole):
    for i, rekord in enumerate(dane):
         el = rekord[pole]
         el = el.replace('zł','') 
         el = el.replace(' ','')
         el = el.replace(',','.')
         rekord[pole] = el
         dane[i] = rekord            #funkcja wpsiująca oczyszczone dane 
        
    return dane
    

def main(args):
    pracownicy = dane_z_pliku('pracownicy.txt')
    pracownicy = wyczysc_dane(pracownicy, 5)
    premia = dane_z_pliku('premia.txt')
    premia = wyczysc_dane(premia, 1)
    dzial = dane_z_pliku('dział.txt')
    
    print(premia)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
