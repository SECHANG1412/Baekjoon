import sys

N = int(sys.stdin.readline())             
liquid = list(map(int, input().split()))  

liquid.sort()  

left= 0       
right= N - 1  

closest_to_zero = sys.maxsize     
best_pair = [0, 0]                

while left < right:
    sum = liquid[left] + liquid[right]

    if abs(sum) < closest_to_zero:
        closest_to_zero = abs(sum)
        best_pair = [liquid[left], liquid[right]]

    if sum < 0:
        left += 1
    elif sum > 0:
        right -= 1
    else:
        break

print(best_pair[0], best_pair[1])
