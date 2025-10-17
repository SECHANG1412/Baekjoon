import sys
input = sys.stdin.readline

n = int(input())
edges = []
total = 0  # 전체 케이블 길이 합

# 케이블 정보 입력 (문자 → 숫자 변환)
for i in range(n):
    row = input().strip()
    for j in range(n):
        if row[j] == '0':
            continue
        # 'a'~'z' → 1~26, 'A'~'Z' → 27~52
        if 'a' <= row[j] <= 'z':
            cost = ord(row[j]) - ord('a') + 1
        else:
            cost = ord(row[j]) - ord('A') + 27
        total += cost
        if i != j:  # 자기 자신 제외
            edges.append((cost, i, j))

# Union-Find (서로소 집합)
parent = [i for i in range(n)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# Kruskal MST (최소 스패닝 트리)
edges.sort()
mst_cost = 0
count = 0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        mst_cost += cost
        count += 1

if count == n - 1:
    print(total - mst_cost)
else:
    print(-1)
