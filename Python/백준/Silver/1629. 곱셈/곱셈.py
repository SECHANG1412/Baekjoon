import sys
sys.setrecursionlimit(10**6)

A, B, C = map(int, sys.stdin.readline().split())

def power(a, b):
    if b == 1:
        return a % C 

    temp = power(a, b // 2)

    if b % 2 == 0:
        return (temp * temp) % C
    else:
        return (temp * temp * a) % C

print(power(A, B))