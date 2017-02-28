#!/usr/bin/python
#-*- coding: UTF-8 -*-

import sys

py_list = []

def py_list_print(list):
    print"[",
    for x in range(0, len(list)):
        sys.stdout.write(str(list[x]))
        if x+1 != len(list):
            print", ",
    print(']')

def py_list_insert(str):
    space_sel=str.find(' ')
    py_list.insert(int(str[:space_sel]),int(str[space_sel:]))

def py_list_remove(var):
    py_list.remove(int(var))

def py_list_append(var):
    py_list.append(int(var))

def py_list_sort():
    py_list.sort()

def py_list_reverse():
    py_list.reverse()

def py_list_pop():
    py_list.pop()

def py_cmd_console(cmd_str):
    space_sel=cmd_str.find(' ')
    if space_sel==-1:
        cmd = cmd_str
    else:
        cmd = cmd_str[:space_sel]

    if cmd=='insert':
        py_list_insert(cmd_str[space_sel+1:])

    elif cmd=='remove':
        py_list_remove(cmd_str[space_sel+1:])

    elif cmd=='append':
        py_list_append(cmd_str[space_sel+1:])

    elif cmd=='print':
        py_list_print(py_list)

    elif cmd=='sort':
        py_list_sort()

    elif cmd=='reverse':
        py_list_reverse()

    elif cmd=='pop':
        py_list_pop()

if __name__ == '__main__':
    N = int(raw_input())
    for i in range(0, N):
        py_cmd_console(str(raw_input()))

