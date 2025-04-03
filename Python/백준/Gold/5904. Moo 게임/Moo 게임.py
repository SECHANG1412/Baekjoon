import sys
sys.setrecursionlimit(10**6)
from functools import lru_cache
input = sys.stdin.readline

def moo(n,k):

    #########
    if k == 0:
        return "moo"[n - 1]

    left=get_len(k-1)
    mid=k+3

    # 왼쪽
    if n<=left:
        return moo(n,k-1)
    
    # 가운데
    elif n<=left+mid:
        return 'm' if n==left+1 else 'o'
    
    # 오른쪽
    else:
        return moo(n-left-mid, k-1)
    
@lru_cache(maxsize=None)
def get_len(k):
    if k==0:
        return 3
    return 2*get_len(k-1)+(k+3)


#####################################################

n=int(input())

# S(k)
k=0
s=3
while s<n:
    k+=1
    s=2*s+(k+3)

print(moo(n, k))
