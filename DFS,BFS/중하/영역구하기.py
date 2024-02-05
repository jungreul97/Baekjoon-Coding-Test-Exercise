import sys
from collections import deque

number = 2
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        if not visited[x][y] and arr[x][y] == 0:
            visited[x][y] = True
            arr[x][y] = number
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                else:
                    if not visited[nx][ny] and arr[nx][ny] == 0:
                        queue.append((nx,ny))
                
n,m,k = map(int,sys.stdin.readline().split())
arr = [ [0] * (m) for j in range(n)]
for _ in range(k):
    square = list(map(int,input().split()))
    for i in range(square[1],square[3]):
        for j in range(square[0],square[2]):
            arr[i][j] = 1
visited = [[False]*m for j in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# print(arr)
# print(visited)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and not visited[i][j]:
            bfs(i,j)
            number+=1
# print(arr)
# print(visited)
print(number-2)

result_arr = []

while number>2:
    result = 0
    number-=1
    for i in range(n):
        result+=arr[i].count(number)
    result_arr.append(result)

result_arr.sort()
for i in result_arr:
    print(i,end= ' ')
        

    
