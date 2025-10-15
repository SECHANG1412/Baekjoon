import sys
from math import gcd
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]

# 1️⃣ 각 재료 간 비율 (p:q) 관계 입력
for _ in range(n - 1):
    a, b, p, q = map(int, input().split())
    graph[a].append((b, p, q))  # a:b = p:q
    graph[b].append((a, q, p))  # b:a = q:p (역방향)

# 2️⃣ 전체 비율의 최소공배수(LCM) 구하기
#    p:q 비율을 모두 정수로 표현하기 위해 LCM 계산
lcm = 1
for a in range(n):
    for b, p, q in graph[a]:
        lcm *= (p * q) // gcd(p, q)
# (모든 비율의 곱을 단순히 누적시켜도 충분함 — 실제 GCD로 나중에 줄여줄 것)

# 3️⃣ DFS로 각 재료 비율 계산
amount = [0] * n
visited = [False] * n
amount[0] = lcm  # 첫 재료 기준 비율 (기준값 설정)

def dfs(node):
    visited[node] = True
    for next_node, p, q in graph[node]:
        if not visited[next_node]:
            # next_node 비율 = 현재 비율 * q / p
            amount[next_node] = amount[node] * q // p
            dfs(next_node)

dfs(0)

# 4️⃣ 전체 재료 비율을 최대공약수로 나눠서 최소 정수화
g = amount[0]
for i in range(1, n):
    g = gcd(g, amount[i])

for i in range(n):
    print(amount[i] // g, end=' ')
