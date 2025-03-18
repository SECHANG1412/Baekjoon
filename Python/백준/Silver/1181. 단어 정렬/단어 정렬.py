n = int(input())  

words = set(input() for i in range(n))
words = list(words)

words.sort() 
words.sort(key=len)

for word in words:
    print(word)
