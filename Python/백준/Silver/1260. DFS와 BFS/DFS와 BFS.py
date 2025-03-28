import sys
from collections import deque

# 스택-후입선출
def dfs(start):
    stack = [start]
    visited = [False] * (N + 1)

    while stack:
        node = stack.pop()

        if not visited[node]:
            visited[node] = True

            print(node, end=" ")
            
            for i in range(N, 0, -1):
                if graph[node][i] and not visited[i]:
                    stack.append(i)

# 큐-선입선출
def bfs(start):
    queue = deque([start])
    visited = [False] * (N + 1)

    while queue:
        node = queue.popleft()

        if not visited[node]:
            visited[node] = True

            print(node, end=" ")
            
            for i in range(1, N + 1):
                if graph[node][i] and not visited[i]:
                    queue.append(i)

#########################################################################

N, M, V = map(int, sys.stdin.readline().split())

graph = [[0] * (N + 1) for _ in range(N + 1)] 
visit_1 = [0] * (N + 1)
visit_2 = [0] * (N + 1)

for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())

  graph[a][b] = graph[b][a] = 1 # 양방향

dfs(V)
print()
bfs(V)