#Uses python2

import sys

def compare(a,b):
    str1 = str(a) + str(b)
    str2 = str(b) + str(a)
    if (int(str1) < int(str2)):
    	return 1
    else:
    	return -1

def largest_number(a):
    #write your code here
    res = sorted(a, cmp = compare)
    return "".join(res)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))