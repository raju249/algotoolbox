# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def dynamic_sequence(n):
    sequence = [sys.maxsize] * (n + 1)
    sequence[1] = 0
    for i in range(2, n + 1):
        sequence[i] = 1 + sequence[i - 1]
        if i % 2 == 0:
            sequence[i] = min(sequence[i], 1 + sequence[i // 2])
        if i % 3 == 0:
            sequence[i] = min(sequence[i], 1 + sequence[i // 3])
    step = sequence[n]
    a = [-1]*(step + 1)
    a[0] = n
    a[step] = 1
    for i in range(1,step):
        if a[i - 1] % 2 == 0 and sequence[a[i - 1] // 2] + 1 == sequence[a[i - 1]]:
            a[i] = a[i - 1] // 2
        elif a[i - 1] % 3 == 0 and sequence[a[i - 1] // 3] + 1 == sequence[a[i - 1]]:
            a[i] = a[i - 1] // 3
        else:
            a[i] = a[i - 1] - 1
    return reversed(a)

input = sys.stdin.read()
n = int(input)
sequence = list(dynamic_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')