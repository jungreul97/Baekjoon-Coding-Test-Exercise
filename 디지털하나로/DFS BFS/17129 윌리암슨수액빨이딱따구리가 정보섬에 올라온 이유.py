import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
start_x,start_y = 0,0
check = False
for i in range(n):
    arr = list(map(int,input().rstrip()))
    if not check and 2 in arr : 
        start_x,start_y = i,arr.index(2)
        check = True
    graph.append(arr)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 0

def dfs(x,y):
    queue = deque()
    queue.append((x,y,0))
    visited = [[False]*m for _ in range(n)]
    visited[x][y] = True

    while queue:
        global result
        x,y,cnt = queue.popleft()
        if graph[x][y] == 3 or graph[x][y] == 4 or graph[x][y] == 5:
            result = cnt
            return True
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and graph[nx][ny] != 1:
                    visited[nx][ny] = True
                    queue.append((nx,ny,cnt+1))
                    
    return False

if dfs(start_x,start_y) :
    print("TAK")
    print(result)
else:
    print("NIE")




