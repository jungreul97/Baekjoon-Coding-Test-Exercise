import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x]) # 그 노드의 부모노드를 찾으러 들어감
    return parent[x]

def union_parent(parent,a,b):#부모노드 다르다면 합치기
    a,b = find_parent(parent,a),find_parent(parent,b)
    if a<b : parent[b] = a
    else : parent[a] = b

V,E = map(int,input().split())

edges = []
parent = [i for i in range(V+1)]

for _ in range(E):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

total = 0
for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b): # 만약 이어진 간선의 부모노드가 다르다면
        union_parent(parent,a,b) # 부모노드 찾기
        total+=cost

print(total)