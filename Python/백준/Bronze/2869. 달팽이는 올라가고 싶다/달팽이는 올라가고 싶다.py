A,B,V = map(int, input().split())

d=(V-A)//(A-B)

if (V-A)%(A-B) !=0: d += 1

print(d+1)