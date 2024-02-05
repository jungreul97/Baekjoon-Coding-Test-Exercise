import sys
from collections import deque
day = 0
def bfs(x,y):
    global day
    queue = deque()
    people = []
    queue.append([x,y])
    people.append([x,y,arr[x][y]])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if not visited[nx][ny] and l<=abs(arr[x][y]-arr[nx][ny])<=r:
                visited[nx][ny] = True
                queue.append([nx,ny])
                people.append([nx,ny,arr[nx][ny]])
    sum = 0
    number = len(people)
    for i in range(number):
        sum+=people[i][2]
    pavg = sum//number
    for i in range(number):
        arr[people[i][0]][people[i][1]] = pavg 
    if number>1:
        day+=1
    
n,l,r = map(int,sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while True:
    visited = [[False]*n for j in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                bfs(i,j)
                print(i,j)
                print(arr)
    if i == n-1 and j == n-1:
        break


print(day)