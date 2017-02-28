import textwrap
from collections import OrderedDict

def merge_the_tools(string, k):
    l = (textwrap.fill(string, k)).split('\n')
    for st in l:
        print "".join(OrderedDict.fromkeys(st))

#if __name__ == '__main__':
#    string,k = raw_input(), int(raw_input())
#    merge_the_tools(string, k)
