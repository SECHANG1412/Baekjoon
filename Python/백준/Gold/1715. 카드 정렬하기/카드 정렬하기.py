import heapq
import sys

n = int(sys.stdin.readline())

cards = [int(input()) for _ in range(n)]

heapq.heapify(cards)  # 카드 묶음 리스트를 최소 힙으로 변환

total = 0

while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    cost = a + b
    total += cost
    heapq.heappush(cards, cost)

print(total)
