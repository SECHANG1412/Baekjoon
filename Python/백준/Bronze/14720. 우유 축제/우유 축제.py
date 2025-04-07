import sys
input=sys.stdin.readline

N=int(input()) #개수
M=list(map(int, input().split())) #종류류

drink=0   #마실 우유
cnt=0     #마신 우유

for i in M:
    if i==drink:
        drink=(drink+1)%3
        cnt+=1

print(cnt)
