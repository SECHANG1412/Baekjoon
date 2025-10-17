import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())  # N: 수 개수, M: 변경 횟수, K: 구간합 질의 횟수
arr = [int(input()) for _ in range(N)]

# 세그먼트 트리 초기화
tree = [0] * (4 * N)

# 트리 구성 함수 (Build)
def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    left = build(node * 2, start, mid)
    right = build(node * 2 + 1, mid + 1, end)
    tree[node] = left + right
    return tree[node]

# 구간 합 쿼리 함수 (Query)
def query(node, start, end, left, right):
    # 범위 벗어난 경우
    if right < start or end < left:
        return 0
    # 범위 완전히 포함
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)

# 값 갱신 함수 (Update)
def update(node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(node * 2, start, mid, idx, diff)
        update(node * 2 + 1, mid + 1, end, idx, diff)

# 트리 초기 구성
build(1, 0, N - 1)

# 쿼리 수행
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:    # 값 변경
        b -= 1
        diff = c - arr[b]
        arr[b] = c
        update(1, 0, N - 1, b, diff)
    elif a == 2:  # 구간 합 출력
        print(query(1, 0, N - 1, b - 1, c - 1))
