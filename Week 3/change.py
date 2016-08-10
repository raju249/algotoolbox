# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = 0
    while m is not 0:
    	if m >= 10:
    		coins += 1
    		m = m - 10
    	elif m >= 5:
    		coins += 1
    		m = m - 5
    	elif m >= 1:
    		coins += 1
    		m = m - 1
    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
