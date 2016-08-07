# Uses python3
import sys

periods = [0,1,1,2,3,5,8,3,1,4,5,9,4,3,7,0,7,7,4,1,5,6,1,7,8,5,3,8,1,9,0,9,9,8,7,5,2,7,9,6,5,1,6,7,3,0,3,3,6,9,5,4,9,3,2,5,7,2,9,1]

def fibonacci_sum(n):
    # write your code here
    sm = 0
    i = 0
    if n <= 60:
        for i in range(0, n + 1):
            sm += periods[i]
        return sm % 10
    else:
        num = n % 60
        sm = sum(periods)
        while i <= num:
            sm += periods[i]
            i += 1
        return sm % 10

    

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
