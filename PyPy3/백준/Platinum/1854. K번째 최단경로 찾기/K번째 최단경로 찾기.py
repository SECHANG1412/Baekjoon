import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M, K = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # 단방향 그래프 (a→b, 가중치 c)

# 거리 리스트 (각 노드별 K개의 최단 거리 저장용)
dist = [[] for _ in range(N + 1)]

# 우선순위 큐 기반 K번째 다익스트라
def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))  # (거리, 시작노드)

    while q:
        cost, now = heapq.heappop(q)

        # 현재 노드에 저장된 K개 이하의 최단거리만 유지
        if len(dist[now]) < K:
            heapq.heappush(dist[now], -cost)  # 최대 힙처럼 음수로 저장
        else:
            # 이미 K개가 있으면 가장 큰 값보다 작을 때만 갱신
            if -dist[now][0] > cost:
                heapq.heappop(dist[now])
                heapq.heappush(dist[now], -cost)
            else:
                continue

        for nxt, w in graph[now]:
            heapq.heappush(q, (cost + w, nxt))

dijkstra()

for i in range(1, N + 1):
    if len(dist[i]) < K:
        print(-1)
    else:
        print(-dist[i][0])  # K번째 최단거리 출력
