a = int(input())  

for _ in range(a):  
    score = list(map(int, input().split())) 

    N = score[0]  
    scores = score[1:]  

    avg=sum(scores)/N

    above_avg=0
    for i in scores:
        if i > avg:
            above_avg+=1

    above=(above_avg/N)*100

    print(f"{above:.3f}%")