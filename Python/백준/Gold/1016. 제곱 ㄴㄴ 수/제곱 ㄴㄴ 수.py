import sys, math
input = sys.stdin.readline

min_val, max_val = map(int, input().split())
length = max_val - min_val + 1

is_square_free = [True] * length

for i in range(2, int(math.sqrt(max_val)) + 1):
    square = i * i
    start = ((min_val + square - 1) // square) * square

    for j in range(start, max_val + 1, square):
        is_square_free[j - min_val] = False

print(is_square_free.count(True))