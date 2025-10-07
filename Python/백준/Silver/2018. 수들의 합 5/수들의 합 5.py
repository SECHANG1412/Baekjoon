n = int(input())
start = 1
end = 1
sum = 1
cnt = 0

while start <= n:
    if sum == n:
        cnt += 1
        sum -= start
        start += 1
    elif sum < n:
        end += 1
        sum += end
    else:  
        sum -= start
        start += 1

print(cnt)
