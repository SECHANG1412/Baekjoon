import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)

def dijkstra(start):
    distance=[INF]*(N+1)
    distance[start]=0

    hq=[]
    heapq.heappush(hq,(0,start))

    while hq:
        current_cost,current_node=heapq.heappop(hq)

        if distance[current_node]<current_cost:
            continue

        for next_node,next_cost in graph[current_node]:
            cost=current_cost+next_cost

            if cost<distance[next_node]:
                distance[next_node]=cost
                heapq.heappush(hq, (cost,next_node))
    return distance

###############################################################

N=int(input())
M=int(input())
graph=[[] for _ in range(N+1)]

for _ in range(M):
    a,b,cost=map(int, input().split())
    graph[a].append([b,cost])

start,end=map(int, input().split())

result=dijkstra(start)
sys.stdout.write(str(result[end]))