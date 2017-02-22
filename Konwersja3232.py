#!/usr/bin/env python
# -*- coding: utf-8 -*-



def konDo10(a, b):
    cyfry = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    wynik = 0

    potega = len(a) - 1

    for i in range(len(a)):
        if b <= 9:
            wynik = wynik + (int(a[i]) * b ** potega)
        else:
            if a[i].upper() in cyfry:
                wynik = wynik + (cyfry[a[i].upper()] * b ** potega)
            else:
                wynik = wynik + (int(a[i]) * b ** potega)
        potega -= 1
    return wynik


def main(args):
    podst = int(raw_input("Podaj podstawe: "))
    liczba_podst = raw_input("Podaj liczbe: ")

    print konDo10(liczba_podst, podst)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
