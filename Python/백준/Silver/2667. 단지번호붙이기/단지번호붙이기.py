import sys
from collections import deque
input=sys.stdin.readline

def bfs(x, y):
    queue = deque()
    queue.append((x, y))    
    visited[x][y] = True
    count = 1   

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1

    return count

########################################################################

n = int(input())

graph = [list(map(int, input().strip())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

#상,하,좌,우
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]: 
            result.append(bfs(i, j))               

result.sort()

print(len(result))

for i in result:
    print(i)
