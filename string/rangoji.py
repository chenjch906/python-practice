#!/usr/bin/python
#-*- coding: UTF-8 -*-


def print_rangoli(size):
    ch = 'a'
    l = []
    for i in range(n):
	for j in range(i+1):
            l.append(chr(ord(ch)+n-j-1))
	for j in reversed(range(i)):
            l.append(chr(ord(ch)+n-j-1))
	print ('-'.join(l)).center(4*(n-1)+1, '-')
	l = []
    for i in reversed(range(n-1)):
	for j in range(i+1):
            l.append(chr(ord(ch)+n-j-1))
	for j in reversed(range(i)):
            l.append(chr(ord(ch)+n-j-1))
	print ('-'.join(l)).center(4*(n-1)+1, '-')
	l = []
