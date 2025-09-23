n = int(input())  
scores = list(map(int, input().split())) 
m = max(scores) 

new_scores = []

for score in scores:
    new_score = (score / m) * 100   
    new_scores.append(new_score)   

average = sum(new_scores) / n

print(average)