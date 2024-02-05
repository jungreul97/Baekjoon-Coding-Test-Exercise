import sys
n = int(sys.stdin.readline())
start,end = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())

arr = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

chon = [0 for i in range(n+1)]
def dfs(v):
    for i in arr[v]:
        if chon[i] == 0:
            chon[i] = chon[v]+1
            dfs(i)

dfs(start)
if chon[end] == 0:
    print(-1)
else:
    print(chon[end])

