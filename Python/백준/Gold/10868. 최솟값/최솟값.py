import sys
input = sys.stdin.readline
INF = 10**9 + 1  # 충분히 큰 수

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# 세그먼트 트리 초기화
tree = [INF] * (4 * N)

# 트리 구성 함수
def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    left = build(node * 2, start, mid)
    right = build(node * 2 + 1, mid + 1, end)
    tree[node] = min(left, right)
    return tree[node]

# 구간 최솟값 쿼리
def query(node, start, end, left, right):
    # 범위 밖
    if right < start or end < left:
        return INF
    # 완전 포함
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    lq = query(node * 2, start, mid, left, right)
    rq = query(node * 2 + 1, mid + 1, end, left, right)
    return min(lq, rq)

# 트리 빌드
build(1, 0, N - 1)

# 쿼리 처리
for _ in range(M):
    a, b = map(int, input().split())
    print(query(1, 0, N - 1, a - 1, b - 1))