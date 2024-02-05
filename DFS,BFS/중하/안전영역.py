import sys
from collections import deque
def bfs(v,x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        if not visited[x][y] and arr[x][y] >= v :
            visited[x][y] = True
            arr[x][y] = number
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    continue
                else:
                    if not visited[nx][ny] and arr[nx][ny] >= v:
                        queue.append((nx,ny))
n = int(sys.stdin.readline())
input_arr=[]
for i in range(n):
    input_arr.append(list(map(int,sys.stdin.readline().split())))
# print(arr)
max_num = 0
min_num = 101
for i in range(n):
    ma = max(input_arr[i])
    mi = min(input_arr[i])
    if max_num<ma:
        max_num = ma
    if min_num>mi:
        min_num = mi
# print(max_num,min_num)
#아무지역도 잠기지 않을때

dx = [-1,1,0,0]
dy = [0,0,-1,1]
min_num+=1
result = 1
while min_num<=max_num:
    # print(min_num,max_num)
    arr = [[j for j in i] for i in input_arr]  
    # print(arr)
    number = 1
    visited = [[False]*n for j in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j]>=min_num:
                bfs(min_num,i,j)
                number+=1 
    if result<number-1:
        result = number-1
    min_num+=1  
    # print(arr)
    
print(result)