import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# BFS로 섬 구분 (각 섬에 고유 번호 부여)
def bfs(x, y, num):
    q = deque([(x, y)])
    graph[x][y] = num
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = num
                q.append((nx, ny))

num = 2  # 섬 번호는 2부터 시작 (1과 구분)
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            bfs(i, j, num)
            num += 1
island_count = num - 2

# 다리 후보 탐색 (두 섬 간 거리)
edges = []

def find_bridge(x, y):
    start = graph[x][y]
    for i in range(4):
        length = 0
        nx, ny = x + dx[i], y + dy[i]
        while 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == start:  # 같은 섬
                break
            if graph[nx][ny] == 0:
                nx += dx[i]
                ny += dy[i]
                length += 1
                continue
            if graph[nx][ny] != start and length >= 2:
                end = graph[nx][ny]
                edges.append((length, start, end))
            break

for i in range(N):
    for j in range(M):
        if graph[i][j] > 1:
            find_bridge(i, j)

# MST (Kruskal)
edges.sort()  # 거리 기준 정렬
parent = [i for i in range(num)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

total = 0
cnt = 0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        total += cost
        cnt += 1

root = find(2)
for i in range(3, num):
    if find(i) != root:
        print(-1)
        sys.exit(0)

print(total)
