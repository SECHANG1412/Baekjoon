import sys

N = int(sys.stdin.readline()) 
A = list(map(int, sys.stdin.readline().split()))[:N]
A = sorted(A)

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))[:M]


for i in B:
    left=0
    right=len(A)-1

    get=False

    while left <= right:
        mid = (left+right)//2
        if A[mid]<i: 
            left=mid+1
        elif A[mid]>i: 
            right=mid-1
        else: 
            get=True 
            break

    if get: 
        print('1')
    else: 
        print('0')