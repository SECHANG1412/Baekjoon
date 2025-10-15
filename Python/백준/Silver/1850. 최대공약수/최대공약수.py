import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

g = gcd(a, b)

print('1' * g)
