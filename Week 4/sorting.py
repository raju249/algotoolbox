# Uses python3
import sys
import random

def partition3(a, start, stop):
    #write your code here
    R = random.Random(42)
    if stop - start < 2:
        return
    key = a[R.randrange(start,stop)]
    e = u = start
    g = stop
    while u < g:
        if a[u] < key:
            swap(a,u,e)
            e = e + 1
            u = u + 1
        elif a[u] == key:
            u = u + 1
        else:
            g = g - 1
            swap(a,u,g)
    partition3(a,start,e)
    partition3(a,g,stop)

def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #randomized_quick_sort(a, 0, n - 1)
    partition3(a,0,len(a))
    for x in a:
        print(x, end=' ')
