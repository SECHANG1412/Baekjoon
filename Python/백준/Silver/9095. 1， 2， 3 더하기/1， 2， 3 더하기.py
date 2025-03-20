T = int(input())  

for _ in range(T):  
    n = int(input())  

    # n=1,2,3일때 값을 고정시킴
    if n == 1: print(1)
    elif n == 2: print(2)
    elif n == 3: print(4)
    
    #n을 4부터 시작
    else:
        list = [0] * (n + 1)
        list[1], list[2], list[3] = 1, 2, 4 
        #list[0]은 무시
        #list[1],[2],[3]은 위 조건에 따라 값을 고정시킴

        for i in range(4, n + 1):
            list[i] = list[i - 3] + list[i - 2] + list[i - 1]  

        print(list[n])  