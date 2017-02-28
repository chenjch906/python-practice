#!/usr/bin/python
#-*- coding: UTF-8 -*-

arr = []
first = -100
second = -100

def get_first_and_second(arr_sel):
    global first
    global second
    if first < arr[arr_sel]:
        second = first
        first = arr[arr_sel]
    elif second < arr[arr_sel]:
        if first != arr[arr_sel]:
            second = arr[arr_sel]

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

    for x in range(n):
        get_first_and_second(x)

    print(second)
