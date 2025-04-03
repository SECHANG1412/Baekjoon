import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(x,y,d):
    stack=[(x,y)]

    while stack:
        ax,ay=stack.pop()

        if visited[ax][ay]:
            continue
        visited[ax][ay]=True

        if d=='-':
            by=ay+1
            if by<M and not visited[ax][by] and graph[ax][by]==d:
                stack.append((ax,by))
        else:
            bx=ax+1
            if bx<N and not visited[bx][ay] and graph[bx][ay]==d:
                stack.append((bx,ay))
            
######################################################

N,M=map(int,input().split())
graph=[list(input().strip()) for _ in range(N)]
visited=[[False]*M for _ in range(N)]

cnt=0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i,j,graph[i][j])
            cnt+=1

print(cnt)