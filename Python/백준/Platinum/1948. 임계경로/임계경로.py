
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())  # 도시 개수
M = int(input())  # 도로 개수

# 1. 그래프 & 역방향 그래프
graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

# 2. 간선 입력
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))         # 정방향 그래프
    reverse_graph[b].append((a, t)) # 역방향 그래프
    indegree[b] += 1

# 3. 출발 도시, 도착 도시
start, end = map(int, input().split())

# 4. 위상 정렬 (최장 경로 구하기)
queue = deque([start])
time = [0] * (N + 1)  # 각 도시까지 걸린 최대 시간

while queue:
    now = queue.popleft()
    for nxt, t in graph[now]:
        if time[nxt] < time[now] + t:
            time[nxt] = time[now] + t
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)

# ✅ end까지 걸린 최대 시간
max_time = time[end]

# 5. 역방향 BFS (임계 경로 간선 개수 구하기)
queue = deque([end])
visited = [False] * (N + 1)
visited[end] = True
cnt = 0

while queue:
    now = queue.popleft()
    for prev, t in reverse_graph[now]:
        # ✅ 실제로 최장 시간에 기여한 간선인지 확인
        if time[prev] + t == time[now]:
            cnt += 1
            if not visited[prev]:
                visited[prev] = True
                queue.append(prev)

print(max_time)
print(cnt)