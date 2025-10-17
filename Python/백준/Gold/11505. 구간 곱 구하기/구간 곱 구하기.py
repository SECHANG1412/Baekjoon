import sys
input = sys.stdin.readline
MOD = 1000000007  # 나머지 연산 상수

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# 세그먼트 트리 초기화
tree = [1] * (4 * N)

# 트리 구성 함수
def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    left = build(node * 2, start, mid)
    right = build(node * 2 + 1, mid + 1, end)
    tree[node] = (left * right) % MOD
    return tree[node]

# 구간 곱 쿼리 함수
def query(node, start, end, left, right):
    # 범위 밖
    if right < start or end < left:
        return 1
    # 범위 완전 포함
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    lq = query(node * 2, start, mid, left, right)
    rq = query(node * 2 + 1, mid + 1, end, left, right)
    return (lq * rq) % MOD

# 값 갱신 함수
def update(node, start, end, idx, val):
    if idx < start or idx > end:
        return
    if start == end:
        tree[node] = val
        return
    mid = (start + end) // 2
    update(node * 2, start, mid, idx, val)
    update(node * 2 + 1, mid + 1, end, idx, val)
    tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD

# 트리 빌드
build(1, 0, N - 1)

# 쿼리 처리
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:  # b번째 수를 c로 변경
        update(1, 0, N - 1, b - 1, c)
    elif a == 2:  # b~c 구간 곱 출력
        print(query(1, 0, N - 1, b - 1, c - 1))