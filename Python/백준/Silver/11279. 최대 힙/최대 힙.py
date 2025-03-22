import sys
import heapq

heap=[]

N = int(sys.stdin.readline())

cnt=0

for _ in range(N):
    n=int(sys.stdin.readline())

    if n>0: 
        heapq.heappush(heap,-n)
        cnt+=1
    elif n==0 and heap:
        print(-heapq.heappop(heap))
        cnt-=1
    else : 
        print(0)
