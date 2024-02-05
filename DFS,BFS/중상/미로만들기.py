import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().strip())))
INF = int(1e9)
visited = [[INF]*(n) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = int(1e9)

def bfs(x,y):
    global result
    queue = deque()
    queue.append((x,y,0))
    visited[x][y] = 0
    while queue:
        x,y,cnt = queue.popleft()
        for i in range(4):
            nx = x+ dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if visited[nx][ny]>cnt+1 and arr[nx][ny] == 0:
                visited[nx][ny] = cnt+1
                queue.append((nx,ny,cnt+1))
            elif visited[nx][ny]>cnt and arr[nx][ny] == 1:
                visited[nx][ny] = cnt
                queue.append((nx,ny,cnt))

bfs(0,0)
# print(visited)
if visited[n-1][n-1] == INF:
    print(0)
else:
    print(visited[n-1][n-1])

