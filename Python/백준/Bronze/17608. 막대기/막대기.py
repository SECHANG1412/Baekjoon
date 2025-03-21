import sys

n = int(sys.stdin.readline()) 

height=[]
result=0

for i in range(n):
    num = int(sys.stdin.readline())
    height.append(num)

max_height=0

for h in reversed(height):
    if h > max_height:
        result+=1
        max_height=h

print(result)
