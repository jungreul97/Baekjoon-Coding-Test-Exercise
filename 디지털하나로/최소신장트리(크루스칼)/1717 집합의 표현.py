import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a,b = find_parent(parent,a),find_parent(parent,b)
    parent[max(a,b)] = min(a,b)

n,m = map(int,input().split())
parent = [i for i in range(n+1)]


for _ in range(m):
    cmd,a,b = map(int,input().split())
    if cmd == 0:
        union_parent(parent,a,b)
    elif cmd == 1:
        if find_parent(parent,a) == find_parent(parent,b):
            print("YES")
        else:
            print("NO")

# print(parent)