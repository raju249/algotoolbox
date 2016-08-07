# Uses python3
import sys

def calc_period(m):
    result = 2;
    fn2 = 1
    fn1 = 2%m
    fn = 3%m
    while fn1 != 1 or fn != 1:
        result += 1
        fn2 = fn1
        fn1 = fn
        fn = (fn1 + fn2)%m
    return result


def calc_fib(n):
    nums = []
    nums.append(0)
    nums.append(1)
    for i in range(2,n + 1):
        nums.append(nums[i - 1] + nums[i - 2])
    return nums[n]

def get_fibonacci_huge(n, m):
    # write your code here
    if n > 4:
        period = calc_period(m)
        num = n % period
        return calc_fib(num) % m
    else:
        num = calc_fib(n)
        return num % m


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
