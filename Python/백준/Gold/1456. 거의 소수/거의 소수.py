import sys
import math

input = sys.stdin.readline

A, B = map(int, input().split())

limit = int(math.sqrt(B)) + 1
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(math.sqrt(limit)) + 1):
    if is_prime[i]:
        for j in range(i * i, limit + 1, i):
            is_prime[j] = False

primes = [i for i in range(2, limit + 1) if is_prime[i]]

count = 0

for p in primes:
    power = p * p 
    while power <= B:
        if power >= A:
            count += 1
        if power > B // p: 
            break
        power *= p

print(count)
