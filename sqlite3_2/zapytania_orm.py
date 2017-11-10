import sqlite3

import os
from peewee import *
from dane import *

baza_plik = "pracownicy.sqlite3"
baza = SqliteDatabase(baza_plik)  # ':memory:'

class BazaModel(Model):  # klasa bazowa
    class Meta:
        database = baza

class Dzial(BazaModel):
    id = IntegerField(primary_key=True)
    nazwa = CharField(null=False)
    siedziba = CharField(null=False)

class Premia(BazaModel):
    id = CharField(primary_key=True)
    premia = DecimalField()

class Pracownik(BazaModel):
    id = CharField(primary_key=True)
    nazwisko = CharField(null=False)
    imie = CharField(null=False)
    stanowisko = ForeignKeyField(Premia, related_name='pracownicy')
    data_zatr = DateField(null=False)
    placa = DecimalField(decimal_places=2)
    premia = DecimalField(decimal_places=2, default=0)
    id_dzial = ForeignKeyField(Dzial, related_name='pracownicy')

baza.connect()

def kw_c():
    query = (Dzial
            .select(Dzial.siedziba, fn.Sum(Pracownik.placa).alias('place'))
            .join(Pracownik)
            .group_by(Dzial.siedziba)
            .order_by('place').asc()
            )

    for obj in query:
        print(obj.siedziba, obj.place)

#kw_c()

def kw_d():
    query = (Pracownik
            .select(Dzial.id, Dzial.nazwa, Pracownik.imie, Pracownik.nazwisko)
            .join(Dzial)
            .order_by(Dzial.nazwa).asc()
            )

    for obj in query:
        print(obj.id_dzial.id, obj.id_dzial.nazwa, obj.imie, obj.nazwisko)

#kw_d()


def kw_e():
    query = (Pracownik
            .select()
            .join(Premia)
            )

    for obj in query:
        print(obj.imie, obj.nazwisko, obj.stanowisko.id, obj.placa * obj.stanowisko.premia)

#kw_e()


def kw_f():
    query = (Pracownik
            .select(fn.Avg(Pracownik.placa).alias('srednia'))
            .group_by(Pracownik.imie.endswith('a'))
            )

    for obj in query:
        print(obj.srednia)

#kw_f()


def kw_g():
    from datetime import datetime
    query = (Pracownik
            .select(Pracownik.imie, Pracownik.nazwisko, Pracownik.stanowisko, Pracownik.data_zatr.year.alias('rok'))
            .join(Premia)
            )

    for obj in query:
        print(obj.imie, obj.nazwisko, obj.stanowisko.id, datetime.now().year - int(obj.rok))

#kw_g()


def kw_h():
    query = (Pracownik
            .select()
            .join(Premia)
            )

    for obj in query:
        print(obj.imie, obj.nazwisko, obj.stanowisko.id, obj.id_dzial.siedziba)

#kw_h()


def kw_i():
    query = (Pracownik
            .select(fn.count(Pracownik.id).alias('ilu'))
            .join(Dzial)
            .group_by(Dzial.siedziba)
            )

    for obj in query:
        print(obj.id_dzial.siedziba)

kw_i()
