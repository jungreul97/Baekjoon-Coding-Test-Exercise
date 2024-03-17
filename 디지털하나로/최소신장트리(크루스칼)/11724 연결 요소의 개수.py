import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)
    if a<b : parent[b] = a
    else : parent[a] = b
N,M = map(int,input().split())

edges = []
parent = [0] * (N+1)

for i in range(1,N+1):
    parent[i] = i

for _ in range(M):
    a,b = map(int,input().split())
    edges.append((a,b))

for edge in edges:
    a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
for i in range(1,N+1):
    parent[i] = find_parent(parent,parent[i])
# print(parent)
print(len(set(parent[1:])))
