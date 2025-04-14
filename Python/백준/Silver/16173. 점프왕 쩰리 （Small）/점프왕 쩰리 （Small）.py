import sys
input=sys.stdin.readline

dx=[1,0] # 아래
dy=[0,1] # 오른쪽

goal=False

def dfs(x,y):
    global goal # 전역변수

    # 종료
    if board[x][y]==-1: 
        goal=True
        return
    
    move=board[x][y]

    for i in range(2):
        nx=x+(dx[i]*move)
        ny=y+(dy[i]*move)

        if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
            visit[nx][ny]=True

            # 다시
            dfs(nx,ny) 

###################################################################

n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]

visit=[[False]*n for _ in range(n)]

visit[0][0]=True
dfs(0, 0)

if goal:
    print('HaruHaru')
else:
    print('Hing')