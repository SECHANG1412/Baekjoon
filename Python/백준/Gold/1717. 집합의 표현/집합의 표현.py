import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

# 1. find 함수 (루트 노드 찾기)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축(Path Compression)
    return parent[x]

# 2. union 함수 (두 집합 합치기)
def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        parent[b_root] = a_root  # 한쪽 루트로 병합

# 3. 입력 처리
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

# 4. 연산 수행
for _ in range(m):
    command, a, b = map(int, input().split())

    if command == 0:
        union(a, b)  # 합집합
    else:
        # 같은 집합이면 YES, 아니면 NO
        print("YES" if find(a) == find(b) else "NO")
