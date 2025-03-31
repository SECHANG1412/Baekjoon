import sys
input = sys.stdin.readline

def dfs(idx, current):
    global max_result, min_result

    # 숫자를 모두 사용-->결과값을 비교해서 최대/최소 저장
    if idx == N:
        max_result = max(max_result, current)
        min_result = min(min_result, current)
        return

    for i in range(4):  
        if cal[i] > 0:   
            cal[i] -= 1  
            
            # 덧셈
            if i == 0:   
                dfs(idx + 1, current + num[idx])

            # 뺄셈
            elif i == 1: 
                dfs(idx + 1, current - num[idx])

            # 곱셈
            elif i == 2: 
                  dfs(idx + 1, current * num[idx])

            # 나눗셈
            elif i == 3: 
                if current < 0:
                    dfs(idx + 1, -(-current // num[idx])) # 음수일 때
                else:
                    dfs(idx + 1, current // num[idx])     # 양수일 때

            cal[i] += 1 

#################################################################

N = int(input())
num = list(map(int, input().split()))  # 숫자 리스트
cal = list(map(int, input().split()))  # 연산 리스트

max_result = -float('inf')  # 최대값
min_result = float('inf')   # 최소값

dfs(1, num[0])

print(max_result)
print(min_result)