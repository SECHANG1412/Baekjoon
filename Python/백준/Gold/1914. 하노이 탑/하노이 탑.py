def hanoi(n, sta, end, temp):
    if n == 1:
        print(f"{sta} {end}")
        return
    hanoi(n - 1, sta, temp, end)
    print(f"{sta} {end}")
    hanoi(n - 1, temp, end, sta)

n = int(input())    
print(2 ** n - 1)

if n <= 20:
    hanoi(n, 1, 3, 2)