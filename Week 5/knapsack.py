# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    rows = len(w)
    cols = W + 1
    a = [[0] * (W + 1) for x in range(len(w))]
    a[0] = [w[0] if w[0] <= j else 0 for j in range(W + 1)]
    for i in range(1, len(w)):
    	for j in range(1, W + 1):
    		value = a[i - 1][j]
    		if w[i] <= j:
    			val = (a[i - 1][j - w[i]]) + w[i]
    			if value < val:
    				value = val
    				a[i][j] = value
    			else:
    				a[i][j] = value
    		else:
    			a[i][j] = value
    return a[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
