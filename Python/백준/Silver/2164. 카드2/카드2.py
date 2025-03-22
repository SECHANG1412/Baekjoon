import sys
from collections import deque
from typing import Any

n = int(sys.stdin.readline()) 


q = deque(list(range(1, n + 1)))
cnt=int(n)

while cnt>1:
    q.popleft()
    q.append(q.popleft())

    cnt-=1
    if cnt==1: 
        break
    
print(q[0])
