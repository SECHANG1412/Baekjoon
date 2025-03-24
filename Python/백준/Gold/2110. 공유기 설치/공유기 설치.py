import sys

N, C = map(int, sys.stdin.readline().split())
x = [int(sys.stdin.readline()) for _ in range(N)]
x.sort()

left = 1              
right = x[-1] - x[0]  
ans = 0               

while left <= right:
    mid = (left + right) // 2  
   
    count = 1         
    last_position = x[0] 

    for i in range(1, N):
        if x[i] - last_position >= mid:
            count += 1
            last_position = x[i]

    if count >= C:
        ans = mid      
        left = mid + 1  
    else:
        right = mid - 1  

print(ans)
