#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  zapytania.py  

import sqlite3



def kw_a(cur):# gdy """ """ przygotowanie zapytania

    cur.execute(""" 
        SELECT nazwisko, imie, tbKlasy.Klasa
        FROM tbuczniowie, tbKlasy
        WHERE tbuczniowie.KlasaID = tbKlasy.IDKlasy
        AND Klasa LIKE '1A'
    """)
    wyniki = cur.fetchall()  #feth - pobierz; fethall - pobierz wszystko
    for row in wyniki:# row - zmienna
        print(tuple(row)) # przekształć i wydrukuj
        
def kw_b(cur):# gdy """ """ przygotowanie zapytania
    cur.execute(""" 
        SELECT  MAX(EgzHum)
        FROM tbuczniowie
        """)
    wyniki = cur.fetchall()#feth - pobierz; fethall - pobierz wszystko
    for row in wyniki:#row - zmienna
        print(tuple(row)) #przekształć i wydrukuj
        
def kw_c(cur):
    cur.execute("""
        SELECT  AVG(EgzMat), tbKlasy.Klasa
        FROM tbuczniowie ,tbKlasy
        WHERE tbuczniowie.KlasaID = tbKlasy.IDKlasy
        AND Klasa LIKE '1A'
    """)
    
    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))
        
def kw_d(cur):
    cur.execute("""
        SELECT Imie, Nazwisko, tbOceny.Ocena, tbPrzedmioty.Przedmiot
        From tbuczniowie, tbOceny ,tbPrzedmioty
        WHERE tbOceny.UczenID = tbuczniowie.IDUcznia
        AND tbOceny.PrzedmiotID = tbPrzedmioty.IDPrzedmiotu
        AND Nazwisko LIKE 'Nowak'
    """)
    
    wyniki = cur.fetchall()#feth - pobierz; fethall - pobierz wszystko
    for row in wyniki:#row - zmienna
        print(tuple(row)) #przekształć i wydrukuj
        
def kw_e(cur):
    cur.execute("""
        SELECT AVG(Ocena), Przedmiot, Datad
        FROM tbOceny, tbPrzedmioty
        WHERE tbOceny.PrzedmiotID = tbPrzedmioty.IDPrzedmiotu 
        AND Przedmiot LIKE 'fizyka'
        AND strftime('%m',datad) LIKE '10'
        
    """)
    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))
        
def main(args):
    con = sqlite3.connect('szkola.db') # połączenie z bazą
    cur = con.cursor() #utworzenie kursora(gdy coś robię w bazie)
    con.row_factory = sqlite3.Row #możliwość odwoływania się do nazwy kolumn
    
    #kw_a(cur)
    #kw_b(cur)
    #kw_c(cur)
    #kw_d(cur)
    kw_e(cur)
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
