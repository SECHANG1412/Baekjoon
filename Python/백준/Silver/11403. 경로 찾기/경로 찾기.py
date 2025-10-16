import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# Floyd-Warshall 변형
for k in range(n):            # 거쳐가는 노드
    for i in range(n):        # 출발 노드
        for j in range(n):    # 도착 노드
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1   # i에서 j로 갈 수 있으면 표시


for i in range(n):
    print(*graph[i])
