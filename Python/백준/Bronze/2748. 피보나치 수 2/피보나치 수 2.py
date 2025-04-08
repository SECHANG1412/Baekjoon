import sys
input=sys.stdin.readline

def fib(n, memo={}):
    if n<=1:
        return n
    
    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


n=int(input())

print(fib(n))