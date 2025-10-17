import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# BFS 함수 정의
def bfs(start):
    visited = [-1] * (N + 1)
    visited[start] = 0
    q = deque([start])

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if visited[nxt] == -1:
                visited[nxt] = visited[now] + 1
                q.append(nxt)
    return sum(visited[1:])  # 모든 사람과의 거리 합

# 최소 케빈 베이컨 수 탐색
answer = float('inf')
person = 0

for i in range(1, N + 1):
    total = bfs(i)
    if total < answer:
        answer = total
        person = i

print(person)
