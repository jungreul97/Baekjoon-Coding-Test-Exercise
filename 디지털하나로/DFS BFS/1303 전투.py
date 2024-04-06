import sys
from collections import deque
input = sys.stdin.readline

M,N = map(int,input().split())
W_total = 0
B_total = 0

arr = []
for _ in range(N):
    arr.append(input().rstrip())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited = [[False]*M for _ in range(N)]

def bfs(ca,x,y):
    queue = deque()
    queue.append((ca,x,y))
    visited[x][y] = True
    result = 1
    while queue:
        c,x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and arr[nx][ny] == c:
                queue.append((c,nx,ny))
                visited[nx][ny] = True
                result += 1
    return result

for i in range(N):
    for j in range(M):
        if not visited[i][j]: 
            if arr[i][j] == 'W': W_total += bfs('W',i,j)**2
            else : B_total += bfs('B',i,j)**2

print(W_total, B_total)