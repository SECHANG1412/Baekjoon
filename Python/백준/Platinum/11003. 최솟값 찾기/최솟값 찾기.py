import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split()) 
arr = list(map(int, input().split()))

dq = deque()

result = []

for i in range(N):

    while dq and arr[dq[-1]] > arr[i]:
        dq.pop()
        
    dq.append(i)

    if dq[0] < i - L + 1:
        dq.popleft()

    result.append(arr[dq[0]])

print(' '.join(map(str, result)))