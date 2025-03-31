import sys
input = sys.stdin.readline

def dfs(index, current):
    global max_result, min_result

    if index == N:
        max_result = max(max_result, current)
        min_result = min(min_result, current)
        return

    for i in range(4):  
        if cal_counts[i] > 0:
            cal_counts[i] -= 1  
            if i == 0:
                dfs(index + 1, current + nums[index])
            elif i == 1:
                dfs(index + 1, current - nums[index])
            elif i == 2:
                dfs(index + 1, current * nums[index])
            elif i == 3:
                if current < 0:
                    dfs(index + 1, -(-current // nums[index]))
                else:
                    dfs(index + 1, current // nums[index])
            cal_counts[i] += 1 


N = int(input())
nums = list(map(int, input().split()))
cal_counts = list(map(int, input().split()))  

max_result = -float('inf')
min_result = float('inf')

dfs(1, nums[0])

print(max_result)
print(min_result)
