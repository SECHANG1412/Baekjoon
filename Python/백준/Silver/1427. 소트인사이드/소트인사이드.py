n = input()   
digits = list(n)

digits.sort(reverse=True)

for i in digits: 
    print(i,end='')