import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)  

V, E = map(int, input().split())  
start = int(input())              

graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())  
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: 
            continue

        for nxt, w in graph[now]:
            cost = dist + w
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))

dijkstra(start)

for i in range(1, V + 1):
    print("INF" if distance[i] == INF else distance[i])