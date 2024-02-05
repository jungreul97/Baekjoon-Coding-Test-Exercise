import sys
from collections import deque
from unittest import result

input = sys.stdin.readline
n,m = map(int,input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

dx = [0,1,0]
dy = [-1,0,1]

visited = [[0]*(m) for _ in range(n)]
answer = 0

def bfs(x,y):
    queue = deque()
    queue.append((x,y,arr[x][y]))
    while queue:
        x,y,result = queue.popleft()
        if x == n-1 and y == m-1:
            if result>answer:
                answer = result
        for i in range(3):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if visited[nx][ny] == 0 or visited[nx][ny]<visited[x][y]+arr[nx][ny]:
                visited[nx][ny] = visited[x][y]+arr[nx][ny]
                result+=arr[nx][ny]
                

        