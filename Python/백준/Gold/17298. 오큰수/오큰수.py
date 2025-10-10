import sys
input = sys.stdin.readline

n = int(input())  
arr = list(map(int, input().split()))  

stack = []  
result = [-1] * n  


for i in range(n):
    while stack and arr[i] > arr[stack[-1]]:
        index = stack.pop()     
        result[index] = arr[i]    

    stack.append(i)
    
print(*result)
