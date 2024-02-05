import sys
from collections import deque

def bfs():
    queue = deque()
    for i in apple:
        queue.append([i[0],i[1],i[2]])
    while queue:
        l,x,y = queue.popleft()
        for i in range(6):
            nh = l+dh[i]
            nx = x+dx[i]
            ny = y+dy[i]
            if nh<0 or nh>=h or nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if arr[nh][nx][ny] == 0 and visited[nh][nx][ny] == 0:
                visited[nh][nx][ny] = visited[l][x][y]+1
                queue.append([nh,nx,ny])
        

m,n,h = map(int,sys.stdin.readline().split())

arr = []
for i in range(h):
    ar = []
    for j in range(n):
        ar.append(list(map(int,input().split())))
    arr.append(ar)

visited = [[[0]*m for j  in range(n)] for i in range(h)]
apple = []
yesapple = False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                visited[i][j][k] = 1
                apple.append([i,j,k])
                yesapple = True
            if arr[i][j][k] == -1:
                visited[i][j][k] = -1

#위,아래,상,하,좌,우
dh = [-1,1,0,0,0,0]
dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,-1,1]

bfs()
# print(visited)
result = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if visited[i][j][k] == 0:
                result = -1
                break
            else:
                if visited[i][j][k]-1>result:
                    result = visited[i][j][k]-1
        if result == -1:
            break
    if result == -1:
        break

if yesapple:
    if result == -1:
        print(result)
    elif arr == visited:
        print(0)
    else:
        print(result)
else:
    print(result)
