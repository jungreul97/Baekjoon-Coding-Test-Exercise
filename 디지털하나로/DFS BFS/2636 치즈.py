import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
cnt = 0
last = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while True:
    queue = deque()
    visited = [[False]*m for _ in range(n)]
    queue.append((0,0))
    arr[0][0] = 2
    visited[0][0] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m :
                continue
            if not visited[nx][ny] and (arr[nx][ny] == 0 or arr[nx][ny] == 2):
                arr[nx][ny] = 2
                visited[nx][ny] = True
                queue.append((nx,ny))
    # print("-----------------------",cnt,"---------------------------------")
    # for i in range(n):
    #     print(*arr[i])
    delete = []
    for i in range(1,n-1):
        for j in range(1,m-1):
            if arr[i][j] == 1 and (arr[i-1][j] == 2 or arr[i+1][j] == 2 or arr[i][j-1] == 2 or arr[i][j+1] == 2):
                delete.append((i,j))
    if len(delete)!=0:
        for i,j in delete:
            arr[i][j] = 0
        last = len(delete)
        cnt+=1
    else:
        break
    # print("-----------------------",cnt,"---------------------------------")
    # for i in range(n):
    #     print(*arr[i])
    # print(delete)

print(cnt)
print(last)