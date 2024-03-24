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
for i in range(N):
    arr = list(map(int,input().split()))
    for j in range(N):
        if arr[j] == 1:
            edges.append((i,j))
arrive = list(map(int,input().split())) # 여행계획
parent = [i for i in range(N)]

for edge in edges :
    a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
arrive_parent = parent[arrive[0]-1] # 1일테니 -1 해서 첫번째 여행지의 부모값 들고오기

for i in arrive:
    if parent[i-1] != arrive_parent: # 여행계획의 도시의 부모가 같지 않다면
        print("NO")
        exit()
print("YES")
    
    