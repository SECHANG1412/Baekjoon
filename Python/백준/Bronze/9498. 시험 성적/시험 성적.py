score=int(input())

if score<0 or score>100: 
    print("잘못입력하셨습니다.")
elif 90<=score<=100: 
    print('A')
elif 80<=score<=89: 
    print('B')
elif 70<=score<=79: 
    print('C')
elif 60<=score<=69: 
    print('D')
else: 
    print('F')