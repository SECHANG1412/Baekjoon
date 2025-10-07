import sys
input = sys.stdin.readline

S, P = map(int, input().split())           
DNA = input().strip()                      
required = list(map(int, input().split())) 

current = [0, 0, 0, 0]  

def char_to_index(ch):
    if ch == 'A':
        return 0
    elif ch == 'C':
        return 1
    elif ch == 'G':
        return 2
    elif ch == 'T':
        return 3

for i in range(P):
    idx = char_to_index(DNA[i])
    current[idx] += 1

def is_valid():
    for i in range(4):
        if current[i] < required[i]:
            return False
    return True

count = 0
if is_valid():
    count += 1

for i in range(P, S):
    left_idx = char_to_index(DNA[i - P])
    current[left_idx] -= 1

    right_idx = char_to_index(DNA[i])
    current[right_idx] += 1

    if is_valid():
        count += 1

print(count)
