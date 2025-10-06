import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

s = [0] * n
c = [0] * m
s[0] = a[0]
ans = 0

for i in range(1, n):
    s[i] = s[i - 1] + a[i]

for i in range(n):
    rem = s[i] % m
    if rem == 0:
        ans += 1
    c[rem] += 1

for i in range(m):
    if c[i] > 1:
        ans += c[i] * (c[i] - 1) // 2

print(ans)