import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

# find 함수 (루트 노드 찾기)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

# union 함수 (두 노드 연결)
def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        parent[b_root] = a_root  # 하나로 합침

N = int(input())  # 도시의 수
M = int(input())  # 여행 계획에 포함된 도시 수

# 부모 배열 초기화
parent = [i for i in range(N + 1)]

# 인접 행렬 입력 및 union 처리
for i in range(1, N + 1):
    row = list(map(int, input().split()))
    for j in range(1, N + 1):
        if row[j - 1] == 1:  # 연결되어 있으면 합침
            union(i, j)

# 여행 계획 입력
plan = list(map(int, input().split()))

# 첫 번째 도시의 루트를 기준으로 비교
root = find(plan[0])
result = all(find(city) == root for city in plan)

print("YES" if result else "NO")