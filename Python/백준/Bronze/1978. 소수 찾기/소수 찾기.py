def prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

n=int(input())
s=map(int, input().split())

result=0
for a in s:
    if prime(a): result+=1

print(result)