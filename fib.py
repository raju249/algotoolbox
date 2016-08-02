# Uses python3
def calc_fib(n):
    nums = []
    nums.append(0)
    nums.append(1)
    for i in range(2,n + 1):
    	nums.append(nums[i - 1] + nums[i - 2])
    return nums[n]

n = int(input())
print(calc_fib(n))
