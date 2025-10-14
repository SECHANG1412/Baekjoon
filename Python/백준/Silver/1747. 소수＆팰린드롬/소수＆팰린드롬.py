import sys
input = sys.stdin.readline

N = int(input())

limit = 1000000
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(limit ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, limit + 1, i):
            is_prime[j] = False

for num in range(N, limit + 1):
    if is_prime[num] and str(num) == str(num)[::-1]:
        print(num)
        break
else:
    print(1003001)  