#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  zapytania.py  

import sqlite3



def kw_c(cur):# gdy """ """ przygotowanie zapytania

    cur.execute(""" 
        SELECT siedziba, SUM(placa) AS pensja
        FROM pracownicy, dzial
        WHERE pracownicy.id_dzial=dzial.id
        GROUP BY siedziba
        ORDER BY pensja ASC
    """)
    wyniki = cur.fetchall()  #feth - pobierz; fethall - pobierz wszystko
    for row in wyniki:# row - zmienna
        print(tuple(row)) # przekształć i wydrukuj
        
def kw_d(cur):# gdy """ """ przygotowanie zapytania
    nazwa = input ("Podaj nazwe dzalu: ")
    siedziba =input ("podaj siedzibę dzialu: ")
    #print(nazwa)
    
    cur.execute(""" 
        SELECT nazwisko,imie, dzial.id, dzial.siedziba, stanowisko
        FROM pracownicy, dzial
        WHERE pracownicy.id_dzial = dzial.id 
        AND dzial.nazwa= ? 
        AND siedziba = ?
        """, (nazwa,siedziba))
        
    wyniki = cur.fetchall()#feth - pobierz; fethall - pobierz wszystko
    for row in wyniki:#row - zmienna
        print(tuple(row)) #przekształć i wydrukuj
        
def kw_e(cur):
    cur.execute("""
        SELECT nazwisko, stanowisko,
        pracownicy.placa *
        (SELECT premia.premia 
        FROM premia
        WHERE pracownicy.stanowisko = premia.id)
        AS premia
        FROM pracownicy
        ORDER BY premia DESC
    """)
    
    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))
        
def kw_f(cur):
    cur.execute("""
        SELECT avg(placa) 
        FROM pracownicy
        WHERE imie LIKE '%a'
    """)
    
    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))
        
    cur.execute("""
        SELECT avg(placa) 
        FROM pracownicy
        WHERE imie NOT LIKE '%a'
    """)
    
    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))
    
def kw_g(cur):
    cur.execute("""
        SELECT imie, nazwisko, stanowisko,
        (JulianDay())
    """)
    
    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))
        
def main(args):
    con = sqlite3.connect('pracownicy.sqlite3') # połączenie z bazą
    cur = con.cursor() #utworzenie kursora(gdy coś robię w bazie)
    con.row_factory = sqlite3.Row #możliwość odwoływania się do nazwy kolumn
    
    kw_g(cur) #PAMIETAJ TO ZMIENIAĆ
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
