import sys
from collections import deque

def bfs(x,y):
    # print(x,y)
    dex = x
    dey = y
    queue = deque()
    queue.append((x,y))
    visited = [[0]*m for i in range(n)]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            else:  
                if nx == dex and ny == dey:
                    continue            
                elif arr[nx][ny] == 'L' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]+1
                    queue.append((nx,ny))
                elif arr[nx][ny] == 'L' and visited[nx][ny]>visited[x][y]+1:
                    visited[nx][ny] = visited[x][y]+1
                    queue.append((nx,ny))
    # print(visited)
    max_num = 0
    for i in visited:
        if max_num<max(i):
            max_num = max(i)
    # print(max_num)
    return max_num   

n,m = map(int,sys.stdin.readline().split())
arr=[]
for i in range(n):
    arr.append(list(input()))
# print(arr)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            answer = bfs(i,j)
            if result<answer:
                result = answer

print(result)


