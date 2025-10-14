import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]

positives = []
negatives = []
ones = 0
zero_exists = False

for num in numbers:
    if num > 1:
        positives.append(num)
    elif num == 1:
        ones += 1
    elif num == 0:
        zero_exists = True
    else:
        negatives.append(num)

positives.sort(reverse=True)

negatives.sort()

total = 0
for i in range(0, len(positives) - 1, 2):
    total += positives[i] * positives[i + 1]

if len(positives) % 2 == 1:
    total += positives[-1]

for i in range(0, len(negatives) - 1, 2):
    total += negatives[i] * negatives[i + 1]

if len(negatives) % 2 == 1:
    if not zero_exists:
        total += negatives[-1]

total += ones

print(total)
