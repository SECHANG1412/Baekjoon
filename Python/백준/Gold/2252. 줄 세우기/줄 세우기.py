import sys
from collections import deque
input=sys.stdin.readline

def topology_sort():
    result=[]
    q=deque()

    for i in range(1,N+1):
        if entry_order[i]==0:
            q.append(i)

    
    while q:
        now=q.popleft()
        result.append(now)

        for i in graph[now]:
            entry_order[i]-=1
            if entry_order[i]==0:
                q.append(i)

    for i in result:
        print(i, end=" ")

#################################################

N,M=map(int, input().split())

entry_order=[0]*(N+1)
graph=[[] for _ in range(N+1)]

for _ in range(M):
    A,B=map(int, input().split())
    graph[A].append(B)
    entry_order[B]+=1

topology_sort()