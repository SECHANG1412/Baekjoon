import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

def bfs(start):
    visited = [False] * (N + 1)
    visited[start] = True
    q = deque([start])
    count = 1  

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                count += 1
                q.append(nxt)
    return count

max_hack = 0
result = []

for i in range(1, N + 1):
    cnt = bfs(i)
    if cnt > max_hack:
        max_hack = cnt
        result = [i]
    elif cnt == max_hack:
        result.append(i)

print(*result)