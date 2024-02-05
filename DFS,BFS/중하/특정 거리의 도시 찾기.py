import sys
from collections import deque

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    distance[v] = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                distance[i] = distance[v]+1
                if distance[i] == k:
                    arr.append(i)
        
    arr.sort()
    if len(arr) == 0:
        print(-1)
    else:
        for i in arr:
            print(i)
    
            
n,m,k,x = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
arr = []
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)

visited = [False] * (n+1)
distance = [0]*(n+1)

visited[x] = True
bfs(x)

