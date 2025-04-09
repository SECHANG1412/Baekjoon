import sys
input=sys.stdin.readline

def lcs(a, b):
    n, m = len(a), len(b)

    # dp[i][j]는 a의 i번째 문자까지와 b의 j번째 문자까지의 LCS 길이
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # DP 테이블 채우기
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                # 문자가 같으면 대각선 왼쪽 위(dp[i-1][j-1]) + 1
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # 다르면 위 또는 왼쪽 중 더 큰 값 선택
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]  # 전체 문자열의 LCS 길이 반환

# 테스트 케이스 2개
a = input().strip()
b = input().strip()
# 결과 출력
print(lcs(a, b))  