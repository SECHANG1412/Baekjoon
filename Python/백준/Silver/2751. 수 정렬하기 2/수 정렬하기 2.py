import sys
input = sys.stdin.readline

n = int(input())

numbers = [int(input().strip()) for _ in range(n)]  
numbers.sort()

sys.stdout.write("\n".join(map(str, numbers)))
