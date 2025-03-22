import sys
from collections import deque
from typing import Any 

N = int(sys.stdin.readline())

queue = deque()
cnt=0

for _ in range(N) :
    ist = list(sys.stdin.readline().split())

    if ist[0] == 'push' :
        queue.append(ist[1])
        cnt += 1

    elif ist[0] == 'size' :
        print(cnt)

    elif ist[0] == 'empty' :
        if cnt == 0 :
            print(1)
        else : 
            print(0)

    ###
    elif ist[0] == 'front':
        if cnt == 0 :
            print(-1)
        else :
            print(queue[0])
    ###
    elif ist[0] == 'back':
        if cnt == 0 :
            print(-1)
        else :
            print(queue[cnt-1])

    ###
    elif ist[0] == 'pop' :
        if cnt == 0 :
            print(-1)
        else :
            cnt -= 1
            print(queue.popleft())
