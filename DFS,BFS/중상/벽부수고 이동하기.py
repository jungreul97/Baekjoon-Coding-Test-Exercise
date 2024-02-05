import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().strip())))
visited = [[[False]*2 for _ in range(m)]for _ in range(n)]
# print(arr)
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y,0,1))
    visited[x][y][1] = True
    while queue:
        x,y,cnt,wall = queue.popleft()
        if x == n-1 and y == m-1:
            return cnt
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            else:
                if visited[nx][ny][wall]:
                    continue
                if arr[nx][ny] == 1 and wall == 1:
                    visited[nx][ny][0] = True
                    queue.append((nx,ny,cnt+1,wall-1))
                elif arr[nx][ny] == 0:
                    visited[nx][ny][wall] = True
                    queue.append((nx,ny,cnt+1,wall))
    return -1

answer = bfs(0,0)
if answer == -1:
    print(answer)
else:
    print(answer+1)
