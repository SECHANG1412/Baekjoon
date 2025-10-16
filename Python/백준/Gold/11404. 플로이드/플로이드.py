import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())        # 도시 개수
m = int(input())        # 버스 개수

# 거리 테이블 초기화
dist = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0  # 자기 자신으로 가는 비용 = 0

# 간선 입력 (중복 노선 중 최소값만 반영)
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:   # 여러 노선 중 더 짧은 것만 유지
        dist[a][b] = c

# Floyd-Warshall 핵심 3중 반복문
for k in range(1, n + 1):      # 거쳐가는 노드
    for i in range(1, n + 1):  # 출발 노드
        for j in range(1, n + 1):  # 도착 노드
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 결과 출력 (INF → 0)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(0 if dist[i][j] == INF else dist[i][j], end=' ')
    print()
