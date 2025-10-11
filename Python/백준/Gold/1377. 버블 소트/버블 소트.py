import sys
input = sys.stdin.readline 

n = int(input())
arr = []

for i in range(n):
    num = int(input())
    arr.append((num, i)) 

arr.sort(key=lambda x: x[0])

max_move = 0
for i in range(n):
    move = arr[i][1] - i
    if move > max_move:
        max_move = move

print(max_move + 1)