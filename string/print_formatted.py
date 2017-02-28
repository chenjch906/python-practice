def print_formatted(num):
    l = len(bin(num)[2:])
    for i in range(num):
        print("%*d %*s %*s %*s"%(l,i+1,l,oct(i+1)[1:],l,hex(i+1)[2:].upper(),l,bin(i+1)[2:]))

if __name__ == '__main__':
    num = int(raw_input())
    print_formatted(num)
