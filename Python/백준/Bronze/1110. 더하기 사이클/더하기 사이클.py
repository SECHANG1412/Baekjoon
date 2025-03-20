n=int(input())            

first=n
cycle_length=0

while True:
    a=n//10     
    b=n%10
    c=(a+b)%10

    n=(b*10)+c

    cycle_length+=1

    if n==first: break

print(cycle_length)