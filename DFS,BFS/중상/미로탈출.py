import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
startx,starty = map(int,sys.stdin.readline().split())
endx,endy = map(int,sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
visited = [[[False]*2 for _ in range(m)]for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y,0,1))
    visited[x][y][1] = True #지팡이 처음에 존재하니까 지팡이 있을때 방문
    while queue:
        x,y,cnt,magic = queue.popleft()
        if x == endx-1 and y == endy-1:
            return cnt
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            else:
                if visited[nx][ny][magic]:
                    continue
                if arr[nx][ny] == 1 and magic == 1:
                    visited[nx][ny][0] = True
                    queue.append((nx,ny,cnt+1,magic-1))
                elif arr[nx][ny] == 0:
                    visited[nx][ny][magic] = True
                    queue.append((nx,ny,cnt+1,magic))

    return -1

print(bfs(startx-1,starty-1))
