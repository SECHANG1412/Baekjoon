import sys
input = sys.stdin.readline

N, M = map(int, input().split())       
lectures = list(map(int, input().split()))

start = max(lectures)                 
end = sum(lectures)                    
answer = end                           

while start <= end:
    mid = (start + end) // 2          
    count = 1                          
    total = 0                          

    for length in lectures:
        if total + length > mid:
            count += 1
            total = 0
        total += length

    if count <= M:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)