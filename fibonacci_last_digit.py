# Uses python3
import sys

def get_fibonacci_last_digit(n):
    nums = []
    nums.append(0)
    nums.append(1)
    for i in range(2,n + 1):
    	nums.append((nums[i - 1] + nums[i - 2]) % 10)
    return nums[n]

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))
