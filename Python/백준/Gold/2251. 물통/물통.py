import sys
from collections import deque
input = sys.stdin.readline

A, B, C = map(int, input().split())

visited = [[False] * (B + 1) for _ in range(A + 1)]
result = set()  

queue = deque([(0, 0, C)])

while queue:
    a, b, c = queue.popleft()

    if visited[a][b]:
        continue
    visited[a][b] = True

    if a == 0:
        result.add(c)

    for from_cup, from_amt, to_cup, to_amt, max_from, max_to in [
        ('A', a, 'B', b, A, B),
        ('A', a, 'C', c, A, C),
        ('B', b, 'A', a, B, A),
        ('B', b, 'C', c, B, C),
        ('C', c, 'A', a, C, A),
        ('C', c, 'B', b, C, B)
    ]:
        move = min(from_amt, max_to - to_amt)
        new_a, new_b, new_c = a, b, c

        if from_cup == 'A': new_a -= move
        if from_cup == 'B': new_b -= move
        if from_cup == 'C': new_c -= move

        if to_cup == 'A': new_a += move
        if to_cup == 'B': new_b += move
        if to_cup == 'C': new_c += move

        queue.append((new_a, new_b, new_c))

print(*sorted(result))