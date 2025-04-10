import sys
input=sys.stdin.readline

n=int(input())

cnt=0

while n>=0:
    if n%5==0:
        cnt=cnt+(n//5)
        break
    
    n-=2
    cnt+=1

if n<0:
    print(-1)
else:
    print(cnt)