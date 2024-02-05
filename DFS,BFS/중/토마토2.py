import sys
from collections import deque

def bfs():
    queue = deque()
    for i in apple:
        queue.append([i[0],i[1]])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if arr[nx][ny] == 0 and visited[nx][ny] == 0 :
                visited[nx][ny] = visited[x][y]+1
                queue.append([nx,ny])

m,n = map(int,sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

apple = []
noapple = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            apple.append([i,j])
            visited[i][j] = 1
        if arr[i][j] == -1:
            noapple.append([i,j])
            visited[i][j] = -1

bfs()
# print(visited)

result = 0
#익은사과가 하나도 없을때
if len(apple) == 0:
    print(-1)
elif arr == visited:
    print(result)
else:
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                result = -1
                break
            if visited[i][j]-1>result:
                result = visited[i][j]-1
        if result == -1:
            break
    print(result)
