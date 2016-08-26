# Uses python3
import sys
import math
def binary_search(a, x):
    low, high = 0, len(a) - 1
    # write your code here
    return binary(a,x,low,high)

def binary(a,x,low,high):
    if high < low:
        return -1
    mid = math.floor(low + (high - low) // 2)
    if x == a[mid]:
        return mid
    elif x < a[mid]:
        return binary(a,x,low,mid - 1)
    else:
        return binary(a,x,mid + 1,high)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
