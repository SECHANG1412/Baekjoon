import sys
input = sys.stdin.readline

def is_prime(num):

    if num < 2: 
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: 
            return False
    return True

def dfs(num, length):
    if length == N:
        print(num)
        return

    for digit in range(1, 10):
        new_num = num * 10 + digit   
        if is_prime(new_num):        
            dfs(new_num, length + 1) 

N = int(input()) 

for prime in [2, 3, 5, 7]:
    dfs(prime, 1)