import sys
input=sys.stdin.readline

N, K = map(int, input().split())

items = []

for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V)) 

dp = [0] * (K + 1)

for weight, value in items:

    for j in range(K, weight - 1, -1):
        dp[j] = max(dp[j], dp[j - weight] + value)

print(dp[K])
