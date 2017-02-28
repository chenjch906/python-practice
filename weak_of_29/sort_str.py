#!/bin/python

import sys

if __name__ == '__main__':
    n = int(raw_input().strip())
    unsorted = []
    unsorted_i = 0
    for unsorted_i in xrange(n):
        unsorted_t = int(raw_input().strip())
        unsorted.append(unsorted_t)

    unsorted.sort()
    for unsorted_i in xrange(n):
        print unsorted[unsorted_i]

