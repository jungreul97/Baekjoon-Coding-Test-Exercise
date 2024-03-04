import sys
import copy
from collections import deque
input = sys.stdin.readline

R,C = map(int,input().split())
graph = []
start_x,start_y = 0,0
end_x,end_y = 0,0
water = []

for i in range(R):
    arr = list(map(str,input().rstrip()))
    for j in range(C):
        if arr[j] == 'S':
            start_x,start_y = i,j
        elif arr[j] == 'D':
            end_x,end_y = i,j
        elif arr[j] == '*':
            water.append([i,j])
    graph.append(arr)

visited = [[-1]*(C) for _ in range(R)]

queue = deque()
for w in water:
    i,j = w[0],w[1]
    queue.append((i,j))
    visited[i][j] = True
queue.append((start_x,start_y))
visited[start_x][start_y] = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while queue:
    x,y = queue.popleft()
    now = graph[x][y]
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if nx<0 or nx>=R or ny<0 or ny>=C:continue
        if visited[nx][ny] != -1: continue
        if graph[nx][ny] == 'X' : continue
        if graph[nx][ny] == '*' : continue
        if now == "*" and graph[nx][ny] == 'D': continue
        if now == 'S':
            if graph[nx][ny] == 'D':
                visited[nx][ny] = visited[x][y] + 1
                break
            visited[nx][ny] = visited[x][y] + 1
        graph[nx][ny] = now
        queue.append((nx,ny))
    
if visited[end_x][end_y] != -1:
    print(visited[end_x][end_y])
else:
    print("KAKTUS")



#런타임 에러 : graph를 시간으로 바꾸고 고슴도치 출발해서 graph의 시간보다 짧으면 목적지로 갈 수 있게 했음
# while queue:
#     x,y,cnt = queue.popleft()
#     for i in range(4):
#         nx,ny = x+dx[i],y+dy[i]
#         if nx<0 or nx>=R or ny<0 or ny>=C:continue
#         if not visited[nx][ny] and graph[nx][ny] == '.':
#             graph[nx][ny] = cnt+1
#             visited[nx][ny] = True
#             queue.append((nx,ny,cnt+1))

# # print(graph)
# visited = [[False]*(C) for _ in range(R)]
# queue.append((start_x,start_y,0))
# visited[start_x][start_y] = True
# while queue:
#     x,y,time = queue.popleft()
#     for i in range(4):
#         nx,ny = x+dx[i],y+dy[i]
#         if nx<0 or nx>=R or ny<0 or ny>=C:continue
#         if graph[nx][ny] == 'D' : result  = min(result,time+1)
#         elif not visited[nx][ny] and graph[nx][ny] != 'X' and graph[nx][ny]>time+1:
#             queue.append((nx,ny,time+1))

# if result!= int(1e9):
#     print(result)
# else:
#     print("KAKTUS")