import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

arr = []
for _ in range(n):
    arr.append(list(map(int,input())))

#상좌하우

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            else:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 2
                    queue.append((nx,ny))
        

for i in range(m):
    if arr[0][i] == 0:
        arr[0][i] = 2
        bfs(0,i)

# print(arr)
result = max(arr[n-1])
if result == 2:
    print("YES")
else:
    print("NO")
    





