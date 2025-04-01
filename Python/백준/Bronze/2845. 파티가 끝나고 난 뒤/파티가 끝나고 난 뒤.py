L, P = map(int, input().split())
articles = list(map(int, input().split()))
for a in articles:
    print(a - L * P, end=' ')
