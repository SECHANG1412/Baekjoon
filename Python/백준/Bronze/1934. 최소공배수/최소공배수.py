import sys
input = sys.stdin.readline

T = int(input()) 

for _ in range(T):
    a, b = map(int, input().split())

    A, B = a, b
    while B != 0:
        A, B = B, A % B

    gcd = A  
    lcm = (a * b) // gcd 

    print(lcm)
