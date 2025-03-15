a=int(input())
for _ in range(a):
    s=input()
    score=0
    total_score=0

    for i in s:
        if i == 'O':
            score+=1
            total_score+=score
        else: score=0

    print(total_score)