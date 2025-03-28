import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    queue = deque([start])
    visited[start] = True  

    while queue:
        node = queue.popleft()

        for i in range(1, N + 1):
            if graph[node][i] and not visited[i]:
                visited[i] = True  
                queue.append(i)

###############################################################

N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1  # 양방향

count = 0

for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)
