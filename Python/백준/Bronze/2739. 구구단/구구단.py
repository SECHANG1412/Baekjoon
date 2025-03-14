while True:
    N=int(input())
    if 1<=N<=9: break 
    print("잘못입력하셨습니다.")

for i in range(1,10):
    print(f"{N} * {i} = {N*i}")
