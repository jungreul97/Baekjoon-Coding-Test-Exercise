import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    global visited
    a,b = find_parent(parent,a),find_parent(parent,b)
    if a == b : return
    parent[max(a,b)] = min(a,b)
    visited[min(a,b)] += visited[max(a,b)] # 기존에 있던거 부모에 관련된 부품 다 더해주고 자기는 초기화
    visited[max(a,b)] = 0

N = int(input())

parent = [i for i in range(1000001)]
visited = [1 for i in range(1000001)]

for _ in range(N):
    arr = list(map(str,input().split()))
    if len(arr) == 3:
        a,b = int(arr[1]),int(arr[2])
        union_parent(parent,a,b)
    else:
        a = int(arr[1])
        print(visited[find_parent(parent,a)])
        
