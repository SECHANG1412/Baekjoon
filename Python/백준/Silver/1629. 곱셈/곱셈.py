import sys
sys.setrecursionlimit(10**6)

A, B, C = map(int, sys.stdin.readline().split())

def power(a,b):
    if b==1:
        return a%C
    
    # 짝수인 경우
    if b%2 == 0:
        half=power(a,b//2)
        return (half*half)%C
    
    # 홀수인 경우
    else:
        half=power(a,b//2)
        return (half*half*a)%C
    
print(power(A,B))