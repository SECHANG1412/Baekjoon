import sys

input=sys.stdin.readline

def largest_rectangle_area(heights):
    stack=[]     
    max_area=0   

    for i in range(len(heights)):
        current_height=heights[i]

        while stack and current_height < stack[-1][1]:
            top_index, top_height = stack.pop()
 

            if not stack:
                width = i 
            else:
                width=i-stack[-1][0]-1

            area=top_height*width
            max_area=max(max_area,area)

        stack.append((i, current_height))
    
    while stack:
        top_index,top_height = stack.pop()

        if not stack:
            width=len(heights)
        else:
            width=len(heights)-stack[-1][0]-1

        area=top_height*width
        max_area=max(max_area, area)
    
    return max_area

while True:
    line=input()
    if not line:
        break
    nums=list(map(int, line.strip().split()))

    if nums[0]==0:
        break

    n=nums[0]
    heights=nums[1:]

    print(largest_rectangle_area(heights))