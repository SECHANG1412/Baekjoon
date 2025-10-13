import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    visited = [-1] * (V + 1) 
    visited[start] = 0         
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for next_node, dist in graph[node]:
            if visited[next_node] == -1:        
                visited[next_node] = visited[node] + dist  
                queue.append(next_node)

    max_distance = max(visited)
    farthest_node = visited.index(max_distance)
    return farthest_node, max_distance

V = int(input())                    
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    data = list(map(int, input().split()))
    node = data[0]
    idx = 1
    while data[idx] != -1:
        neighbor = data[idx]
        weight = data[idx + 1]
        graph[node].append((neighbor, weight))
        idx += 2

node_a, _ = bfs(1)

_, diameter = bfs(node_a)

print(diameter)
