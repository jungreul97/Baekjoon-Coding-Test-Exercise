import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a,b = find_parent(parent,a),find_parent(parent,b)
    parent[max(a,b)] = min(a,b)



V,E = map(int,input().split())

edges = []
parent = [0]*(V+1)

for i in range(1,V+1):
    parent[i] = i

for _ in range(E):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()
total = 0
for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        total+=cost
print(parent)
print(total)