import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(node, depth):
    global found

    if depth == 5:
        found = True
        return
    
    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, depth + 1)
            if found:
                return
            
    visited[node] = False  

#################################################################
N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * N
found = False

for i in range(N):
    dfs(i, 1)
    if found:
        break

print(1 if found else 0)
