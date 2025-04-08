import sys
input=sys.stdin.readline

def tile(N):
    dp=[0]*(N+2) 
    dp[1]=1
    dp[2]=2

    for i in range(3, N + 1):
        dp[i]=(dp[i-1]+dp[i-2]) % 15746

    return dp[N]

N=int(input())

print(tile(N))