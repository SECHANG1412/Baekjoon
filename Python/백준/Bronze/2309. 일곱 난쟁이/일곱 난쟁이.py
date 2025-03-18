ds = [int(input()) for _ in range(9)] 

total_height = sum(ds)

# 브루트포스 탐색
for i in range(9):
    for j in range(i + 1, 9):  
        if total_height - ds[i] - ds[j] == 100:
            fake1, fake2 = ds[i], ds[j]  
            ds.remove(fake1)  
            ds.remove(fake2)
            ds.sort()  

            for d in ds:
                print(d)

            exit()