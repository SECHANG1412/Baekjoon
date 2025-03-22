from collections import deque

N = int(input())  
K = int(input())

board = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1  

L = int(input())
turns = {}
for _ in range(L):
    X, C = input().split()
    turns[int(X)] = C

# 방향: 오른쪽, 아래, 왼쪽, 위 (시계방향)
dx = [0, 1, 0, -1]  # 행
dy = [1, 0, -1, 0]  # 열
direction = 0  

snake = deque()
snake.append((0, 0))  

snake_positions = set()     
snake_positions.add((0, 0))

time = 0
x, y = 0, 0  

while True:
    time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    if not (0 <= nx < N and 0 <= ny < N) or (nx, ny) in snake_positions:
        print(time)
        break

    snake.append((nx, ny))          
    snake_positions.add((nx, ny))   

    if board[nx][ny] == 1:
        board[nx][ny] = 0  
    else:
        tail = snake.popleft()
        snake_positions.remove(tail)

    if time in turns:
        if turns[time] == 'D':  
            direction = (direction + 1) % 4
        else:  
            direction = (direction - 1 + 4) % 4

    x, y = nx, ny
