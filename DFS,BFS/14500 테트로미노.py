from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = 0

for i in range(n):
    for j in range(m):
        queue = deque()
        visited = [[False]*m for j in range(n)]
        queue.append((i,j,arr[i][j],1))
        visited[i][j] = True
        while queue:
            x,y,sum,cnt = queue.popleft()
            if cnt == 4:
                if result<sum:
                    result = sum
                    break
            else:
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]

                    if nx<0 or nx>=n or ny<0 or ny>=m:
                        continue

                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx,ny,sum+arr[nx][ny],cnt+1))

print(result)
