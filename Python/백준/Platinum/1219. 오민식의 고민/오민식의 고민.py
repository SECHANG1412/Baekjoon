import sys
input = sys.stdin.readline
INF = int(1e18)

N, start, end, M = map(int, input().split())

edges = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))

# 각 도시의 수익
earn = list(map(int, input().split()))

# 초기화
dist = [-INF] * N
dist[start] = earn[start]  # 출발 도시는 벌 수 있는 돈으로 시작

# Bellman-Ford (N-1번 완화)
for i in range(N - 1):
    for a, b, cost in edges:
        if dist[a] == -INF:
            continue
        # a→b 이동 시 이익 계산: dist[a] - 이동비용 + 도착도시 이익
        if dist[b] < dist[a] - cost + earn[b]:
            dist[b] = dist[a] - cost + earn[b]

# 양의 사이클(무한 이익 루프) 탐지 및 전파
cycle = [False] * N
for i in range(N):
    for a, b, cost in edges:
        if dist[a] == -INF:
            continue
        if dist[b] < dist[a] - cost + earn[b]:
            dist[b] = dist[a] - cost + earn[b]
            cycle[b] = True
            cycle[a] = True

# 사이클 전파 (연결된 노드들도 무한 이익 루프면 표시)
for i in range(N):
    for a, b, cost in edges:
        if cycle[a]:
            cycle[b] = True

# 결과 판별
if dist[end] == -INF:
    print("gg")  # 도착 불가
elif cycle[end]:
    print("Gee")  # 무한히 돈을 벌 수 있음
else:
    print(dist[end])  # 최대 수익 출력
