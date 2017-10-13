#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendaD.py 

import sqlite3

ef kw_d(cur):
    cur.execute("""
        SELECT stanowisko AS kierownik
        FROM pracownicy
    """)
    
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
