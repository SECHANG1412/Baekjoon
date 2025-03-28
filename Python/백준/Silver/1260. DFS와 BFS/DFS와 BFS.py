import sys
from collections import deque

# 스택
def dfs(start):
    stack = [start]          
    visit1 = [0] * (N + 1)  
    while stack:
        v = stack.pop()      
        if not visit1[v]:
            visit1[v] = 1
            print(v, end=" ")
            for i in range(N, 0, -1):
                if not visit1[i] and graph[v][i] == 1:
                    stack.append(i)


# 큐
def bfs(V):
  queue = deque()
  queue.append(V)       
  visit2[V] = 1

  while queue:
    V = queue.popleft()
    print(V, end = " ")
    for i in range(1, N + 1):
      if visit2[i] == 0 and graph[V][i] == 1:
        queue.append(i)
        visit2[i] = 1

##############################################################

N, M, V = map(int, sys.stdin.readline().split())

graph = [[0] * (N + 1) for _ in range(N + 1)] 
visit1 = [0] * (N + 1)
visit2 = [0] * (N + 1)

for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  graph[a][b] = graph[b][a] = 1

dfs(V)
print()
bfs(V)