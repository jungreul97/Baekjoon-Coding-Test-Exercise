import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
start_x,start_y,command = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
#북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

queue = deque()
queue.append((start_x,start_y,command))
visited = [[False]*M for _ in range(N)]
visited[start_x][start_y] = True
while queue:
    x,y,cmd = queue.popleft()
    check = False # 사방이 벽이거나 모두 청소했을경우 가지못하므로 false
    tmp = 0
    while not check and tmp<4:
        cmd = cmd-1
        if cmd == -1: cmd = 3
        nx,ny = x+dx[cmd],y+dy[cmd]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and arr[nx][ny] == 0:
            check = True
            visited[nx][ny] = True
            queue.append((nx,ny,cmd))
        tmp+=1
    if not check:
        cmd = (cmd+2)%4
        nx,ny = x+dx[cmd],y+dy[cmd]
        if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 0:
            queue.append((nx,ny,cmd))
        else:
            break

print(visited)
answer = 0
for i in range(N):
    answer += visited[i].count(True)
print(answer)


