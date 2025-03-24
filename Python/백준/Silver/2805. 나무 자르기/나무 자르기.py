import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

if sum(A) < M:
    print("잘못입력!")
else:
    left, right = 0, max(A)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        total = sum(i - mid for i in A if i > mid)

        if total >= M:
            result = mid  # 현재 높이로도 가능한데, 더 높여볼 수 있음
            left = mid + 1
        else:
            right = mid - 1

    print(result)