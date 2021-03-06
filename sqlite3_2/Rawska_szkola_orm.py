#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  zapytania.py

import sqlite3

import os
from peewee import *
from dane import *

baza_plik = "pracownicy.sqlite3"
baza = SqliteDatabase(baza_plik)

class BazaModel(Model):  # klasa bazowa
    class Meta:
        database = baza

class Klasa(BazaModel):
    klasa = CharField(null=False)
    rok_naboru = IntegerField(null=False)
    rok_matury = IntegerField(null=False)

class Przedmiot(BazaModel):
    przedmiot = CharField(null=False)
    nazwiskon = CharField(null=False)
    imien = CharField(null=False)
    plecn = IntegerField()

class Ocena(BazaModel):
    datad = DateField(null=False)
    uczen_id = ForeignKeyField(Uczen, related_name='szkola')
    przedmiot_id = ForeignKeyField(Przedmiot, related_name='szkola')
    ocena = DecimalField(null=False)

class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = IntegerField(null=False)
    klasa_id = ForeignKeyField(Klasa, related_name='szkola')
    egzhum = IntegerField(null=False)
    egzmat = IntegerField(null=False)
    egzjez = IntegerField(null=False)


baza.connect()

def kwerenda_a():
    query=(Dzial
        .select(uczen.imie, uczen.nazwisko)
        .group_by(klasa_id = "1A")
        )
    for obj in query:
        print(uczen.imie, uczen.nazwisko)


kwerenda_a()


















def wyniki(cur):
   wyniki = cur.fetchall()
   for row in wyniki:
        print(tuple(row))

def dodaj(cur):
    cur.execute("""
        INSERT INTO tbKlasy
        VALUES (?, ?, ?, ?)
    """,[None, '3C', 2015, 2017])

def aktualizuj(cur):
    cur.execute("""
        UPDATE tbKlasy
        SET klasa = ?
        WHERE idklasy = 1?
    """,['3D', 13])

def usun(cur):
    cur.execute('DELETE FROM tbKlasy WHERE klasa = ? AND roknaboru = ?', ['3B', 2015])

def aktualizuj2(cur):
    cur.execute("""
        UPDATE tbUczniowie
        SET EgzJez = ?
        WHERE nazwisko LIKE 'Dziedzic'
    """,['Paulina Dziedzic' 35])

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
    #kw_e(cur)

    #dodaj(cur)
    #aktualizuj(cur)
    #usun(cur)
    aktualizuj2(cur)
    con.commit()
    wyniki(cur.execute('SELECT * FROM tbklasy'))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
