import sys

def dfs(v):
    stack = [v]
    visited = [False] * (A + 1)
    count = 0  # 감염 컴퓨터 수 (1번 제외 예정)

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            count += 1  
            for i in range(A, 0, -1): 
                if graph[node][i] == 1 and not visited[i]:
                    stack.append(i)
    return count - 1  # 1번 컴퓨터 제외

##########################################################################

A = int(sys.stdin.readline())  
B = int(sys.stdin.readline())  


graph = [[0] * (A + 1) for _ in range(A + 1)]

for _ in range(B):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1  # 양방향 

print(dfs(1))
