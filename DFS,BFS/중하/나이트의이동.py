from collections import deque
def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        start = queue.popleft()
        x = start[0]
        y = start[1]
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            else:
                if nx == end[0] and ny == end[1]:
                    arr[nx][ny] = arr[x][y]+1
                    return
                #가장 빨리 가는것만 저장
                elif arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y]+1
                    queue.append([nx,ny])
    return

t = int(input())
dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,-2,-1,1,2]

for _ in range(t):
    n = int(input())
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    arr = [[0 for i in range(n)]for j in range(n)]  
    if start == end:
        print(0)
    else:
        bfs(start)
        print(arr[end[0]][end[1]])



