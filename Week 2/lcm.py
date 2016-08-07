# Uses python3
import sys

def gcd(a,b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

def lcm(a, b):
    #write your code here
    ans = gcd(a,b)
    return (a*b) // ans

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

