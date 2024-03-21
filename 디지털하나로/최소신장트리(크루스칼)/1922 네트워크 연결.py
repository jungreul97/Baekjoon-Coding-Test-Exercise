import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a,b = find_parent(parent,a),find_parent(parent,b)
    parent[max(a,b)] = min(a,b)

N = int(input())
M = int(input())
edges = []
for _ in range(M):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

parent = [i for i in range(N+1)]
answer = 0

edges.sort()

for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        answer += cost

print(answer)