#!/usr/bin/python
#-*- coding: UTF-8 -*-

py_tuple = ()

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())

    py_tuple = tuple(integer_list)
    print(hash(py_tuple))
