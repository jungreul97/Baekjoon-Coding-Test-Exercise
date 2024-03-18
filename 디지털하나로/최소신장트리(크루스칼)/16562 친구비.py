import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]  

def union_parent(parent,a,b):
    a,b = find_parent(parent,a),find_parent(parent,b) # 부모 찾고
    if a == b: return
    if moneys[a]<moneys[b]  : 
        parent[b] = a
        moneys[b] = 0 # 부모노드가 아니면 비용을 0으로 만들기
    else : 
        parent[a] = b
        moneys[a] = 0

N,M,k = map(int,(input().split()))
moneys = [0]+list(map(int,input().split()))
edges = []
parent = [i for i in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    union_parent(parent,a,b) # 어차피 연결되어 있으니까 둘중에 최소만 남김
print(parent)
print(moneys)
total = sum(moneys)

if k<total: print("Oh no")
else : print(total)
