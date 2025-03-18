width, height = map(int, input().split())
n = int(input()) 

width_line = [0, height]  
height_line = [0, width]  


for _ in range(n):
    width_point, height_point = map(int, input().split())
    if width_point == 0:
        width_line.append(height_point)  
    else:
        height_line.append(height_point)  

width_line.sort()
height_line.sort()

max_height = max(width_line[i] - width_line[i-1] for i in range(1, len(width_line)))

max_width = max(height_line[i] - height_line[i-1] for i in range(1, len(height_line)))

print(max_width * max_height)
