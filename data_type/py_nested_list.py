#!/usr/bin/python
#-*- coding: UTF-8 -*-

import operator

arr = []

if __name__ == '__main__':
    priv = 0
    lowest = 0
    num = int(raw_input())
    for i in range(num):
        name = raw_input()
        score = float(raw_input())
        arr.append([name, score])

    arr.sort(key=operator.itemgetter(1), reverse=True)
    for i in range(num):
        print arr[i]
    for i in range(num):
        re_sel = num - i - 1
        if lowest == 1:
            print arr[re_sel][0]
        if arr[re_sel][1] != arr[re_sel-1][1]:
            lowest += 1
        if i+1 >= num-1:
            if lowest == 1:
                print arr[re_sel-1][0]
            break
