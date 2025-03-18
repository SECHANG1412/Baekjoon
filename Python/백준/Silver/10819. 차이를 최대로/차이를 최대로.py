from itertools import permutations

N = int(input())  
A = list(map(int, input().split()))  

all_permutations = permutations(A)  

max_value = 0  

for perm in all_permutations:
    total = sum(abs(perm[i] - perm[i + 1]) for i in range(N - 1))  
    max_value = max(max_value, total)  

print(max_value)