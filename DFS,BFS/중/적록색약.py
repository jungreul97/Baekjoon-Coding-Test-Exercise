import sys
from collections import deque

def bfs(x,y):
    global number
    queue = deque()
    queue.append([x,y])
    s = arr[x][y]
    visited[x][y] = number
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if arr[nx][ny] == s and visited[nx][ny] == 0:
                visited[nx][ny] = number
                queue.append([nx,ny])
        
def bfs_blue(x,y):
    queue = deque()
    queue.append([x,y])
    visited[x][y] = number_blue
    s = arr[x][y]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if s !='B':
                if arr[nx][ny]!='B' and visited[nx][ny] == 0:
                    visited[nx][ny] = number_blue
                    queue.append([nx,ny])
            else:
                if arr[nx][ny] == 'B' and visited[nx][ny] == 0:
                    visited[nx][ny] = number_blue
                    queue.append([nx,ny])

n = int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(list(input()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

number = 1
visited = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j)
            number+=1
# print(visited)

number_blue = 1
visited = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs_blue(i,j)
            number_blue+=1
# print(visited)    

print(number-1,number_blue-1)