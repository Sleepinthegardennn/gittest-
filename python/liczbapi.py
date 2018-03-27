#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def main(args):
    ileKw = int(input("Podaj liczbe: "))
    ileKo = 0
    r = 1

    for i in range(ileKw):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= r**2:
            ileKo += 1
    pi = 4 * ileKo/ ileKw
    print("Przyblizona wartośc liczby pi: ", pi)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
