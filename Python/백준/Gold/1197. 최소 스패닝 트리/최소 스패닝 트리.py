import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent, a)
    b=find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

V, E = map(int, input().split())

parent = [i for i in range(V + 1)]

edge=[]

edge = []
for _ in range(E):
    a, b, cost = map(int, input().split())
    edge.append((cost, a, b))

edge.sort()
total=0

for cost,a,b in edge:
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        total+=cost

print(total)