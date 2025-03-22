import sys
from collections import deque
from typing import Any 

N, K = map(int, sys.stdin.readline().split())
people = deque(list(range(1, N + 1)))

cnt=int(N)

result= []

while cnt>0:
    for _ in range(K-1):
        people.append(people.popleft())
    
    remove = people.popleft()
    result.append(remove)
    cnt-=1
    

print("<" + ", ".join(map(str, result)) + ">")