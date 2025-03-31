import sys
sys.setrecursionlimit(10**6)

def dfs(start):
    visited[start] = True
    inside_count = 0
    for v in graph[start]:
        if inside[v] == '1': 
            inside_count += 1
        elif not visited[v] and inside[i] == "0":
            inside_count += dfs(v)
    return inside_count

##########################################################

N = int(input())
inside = '0' + input()
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
total = 0

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    if inside[a] == "1" and inside[b] == "1":
        total += 2

for i in range(1, N+1):
    if inside[i] == '0' and not visited[i]:
        result = dfs(i)
        total += (result) * (result - 1)

print(total)
