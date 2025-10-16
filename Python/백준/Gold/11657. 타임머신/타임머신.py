import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())  # N: 도시 수, M: 버스 노선 수
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))  # a→b, 가중치 c (시간)

# 거리 초기화
distance = [INF] * (N + 1)
distance[1] = 0  # 출발점은 1번 도시

# Bellman-Ford 알고리즘
# 모든 간선을 N-1번 반복하며 최단 거리 갱신
for i in range(N - 1):
    for a, b, c in edges:
        if distance[a] != INF and distance[b] > distance[a] + c:
            distance[b] = distance[a] + c

# 음수 사이클 존재 여부 확인 (N번째 반복에서 갱신 발생 시)
cycle = False
for a, b, c in edges:
    if distance[a] != INF and distance[b] > distance[a] + c:
        cycle = True
        break

if cycle:
    print(-1)  # 음수 사이클 존재
else:
    for i in range(2, N + 1):
        print(distance[i] if distance[i] != INF else -1)
