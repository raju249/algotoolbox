# Uses python3
def edit_distance(s, t):
    #write your code here
    if s == t:
    	return 0

    sLen = len(s)
    tLen = len(t)
    s = "#" + s
    t = "#" + t
    a = [[0] * (sLen + 1) for i in range(tLen + 1)]
    a[0] = [i for i in range(0, sLen + 1)]
    for j in range(0, tLen + 1):
    	a[j][0] = j
    for i in range(1, tLen  + 1):
    	for j in range(1, sLen + 1):
    		if t[i] == s[j]:
    			a[i][j] = a[i - 1][j - 1]
    		else:
    			a[i][j] = 1 + min(a[i - 1][j - 1], a[i][ j - 1], a[i - 1][j])
    return a[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
