#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  format.py
#  


def main(args):
    print("{}{}".format(1, 2))
    print("{1:>20}{0:>10}".format(1, 2))
    print("{1:_>20}{0:.>10}".format(1, 2))
    print("{1:_^20}{0:.^10}".format(1, 2))
    
    print("{:10.5f}".format(3.14159265))
    print("{:*^30.5f}".format(3.14159265))
    
    print(hex(100))
    print(oct(100))
    print(bin(100))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
