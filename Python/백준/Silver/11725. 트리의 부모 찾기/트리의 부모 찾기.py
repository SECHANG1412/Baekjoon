import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 스택
def dfs(start):
    stack = [start]

    while stack:
        node = stack.pop()

        if not visited[node]:
            visited[node] = True

            for next_node in graph[node]:
                if not visited[next_node]:
                    parent[next_node] = node
                    stack.append(next_node)

############################################################################

N = int(input().strip())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N + 1) 
visited = [False] * (N + 1)

dfs(1)

# 2번 노드부터 N번 노드까지 부모 노드를 출력
for i in range(2, N + 1):
    print(parent[i])