import sys
sys.setrecursionlimit(10 ** 6) 

def postorder(start,end):
    if start>end:
        return
   
    mid = end+1 
    for i in range(start+1,end+1):
        if a[start]<a[i]:
            mid = i 
            break
    
    # 전위: 왼쪽->오른쪽->루트
    postorder(start+1, mid-1)  # 왼쪽 서브트리
    postorder(mid, end)        # 오른쪽 서브트리   
    print(a[start])            # 루트


a=[]
while True: 
    try:
        a.append(int(sys.stdin.readline()))
    except: 
        break

postorder(0,len(a)-1)