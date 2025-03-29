import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    distance[start] = 0  # 시작 도시의 거리는 0
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            # 아직 방문하지 않았다면 (방문 여부 대신 distance 값이 -1 인지 확인)
            if distance[next_node] == -1:
                distance[next_node] = distance[node] + 1
                queue.append(next_node)

N, M, K, X = map(int, input().split())

# 인접 리스트 사용 (메모리 효율적)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# distance 배열 초기화 (방문하지 않은 경우 -1)
distance = [-1] * (N + 1)

# BFS 실행 (출발 도시 X부터 탐색)
bfs(X)

# 결과 출력: 거리가 K인 도시를 모두 모아서 출력
result = []
for i in range(1, N + 1):
    if distance[i] == K:
        result.append(str(i))

if result:
    sys.stdout.write("\n".join(result))
else:
    sys.stdout.write("-1")
