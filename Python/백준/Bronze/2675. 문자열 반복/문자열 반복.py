n =int(input())

for _ in range(n):
    R,S = input().split()
    R=int(R)

    result=''
    for i in S: result = result+(i*R)
    print(result)