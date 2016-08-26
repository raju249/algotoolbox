# Uses python3
import sys

def get_majority_element(a, left, right):
    count = 0
    maj = -1
    l = len(a)
    for i in range(l):
        if count == 0:
            maj = a[i]
        if a[i] == maj:
            count += 1
        else:
            count -= 1

    count = 0
    for i in range(l):
        if a[i] == maj:
            count += 1
        if count > l//2:
            return 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
