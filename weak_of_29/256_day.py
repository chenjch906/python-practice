#!/bin/python

import sys

def check_leap_year(y):
    if y < 1917:
        if y%4 == 0:
            return 1
    else:
        if (y%4 == 0 and y%100 != 0) or y%400 == 0:
            return 1
    return 0

if __name__ == '__main__':
    y = int(raw_input().strip())
    leap = check_leap_year(y)

    if leap == 1:
        print ("12.09.%4d"%(y))
    else:
        print ("13.09.%4d"%(y))
