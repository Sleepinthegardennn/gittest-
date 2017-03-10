#!/usr/bin/env python
# -*- coding: utf-8 -*-


def szyfruj_cezar(tekst, klucz):
    klucz = klucz % 26
    szyfrogram = ''
    for znak in tekst:
        znak = znak.lower()
        if ord(znak) + klucz > 122:
            szyfrogram += chr(ord(znak) + klucz - 26)
        else:
            szyfrogram += chr(ord(znak) + klucz)
    return szyfrogram


def deszyfruj_cezar(szyfrogram, klucz):
    tekst = ""
    pass
    return tekst


def main(args):
    tekst = raw_input("Podaj tekst: ")
    klucz = int(raw_input("POdaj klucz: "))
    szyfrogram = szyfruj_cezar(tekst, klucz)
    print szyfrogram
    print deszyfruj_cezar(szyfrogram, klucz)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
