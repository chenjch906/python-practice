#!/bin/python

import textwrap

def swap_case(s):
    i = 0
    l = list(s)
    for c in l:
        if c.islower():
            l[i] = c.upper()
        elif c.isupper():
            l[i] = c.lower()
        i += 1
    return ''.join(l)

def split_and_join(s):
    l = s.split()
    return '-'.join(l)

def print_full_name(a, b):
    print("Hello %s %s! You just delved into python."%(a,b))

def mutate_string(string, pos, char):
    l = list(s)
    l[pos] = char
    return ''.join(l)

def count_substring(string, sub):
    i = 0
    count = 0
    l = len(string)
    while i < l-1:
        pos = string[i:l].find(sub)
        if pos >= 0:
            count += 1
        else:
            break
        i  = pos + i + 1
    return count

def str_check(s):
    alnum = 'False'
    alpha = 'False'
    digit = 'False'
    lower = 'False'
    upper = 'False'

    for c in s:
        if c.isalnum():
            alnum = 'True'
        if c.isalpha():
            alpha = 'True'
        if c.isdigit():
            digit = 'True'
        if c.islower():
            lower = 'True'
        if c.isupper():
            upper = 'True'

    print alnum
    print alpha
    print digit
    print lower
    print upper

def wrap(string, max_w):
   return textwrap.fill(string, max_w)

def capitalize(string):
    i = 0
    n = 0
    beg = 0
    end = len(string)
    l = list(string)
    for i in range(end-1):
        if i == 0 and l[i].islower():
            l[i] = l[i].upper()
        if l[i] == ' ' and l[i+1] != ' ' and l[i+1].islower():
            l[i+1] = l[i+1].upper()

    return ''.join(l)
  #  return string.title()

if __name__ == '__main__':
    a = raw_input()
    print capitalize(a)
