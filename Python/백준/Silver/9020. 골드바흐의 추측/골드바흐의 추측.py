def prime_sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime

T = int(input())
nums = [int(input()) for _ in range(T)]

is_prime = prime_sieve(10000)

for n in nums:
    for i in range(n // 2, 1, -1):
        if is_prime[i] and is_prime[n - i]:
            print(i, n - i)
            break