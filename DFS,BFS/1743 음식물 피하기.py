import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline

n,m,k = map(int,input().split())

arr = [[0]*(m+1) for _ in range(n+1)]
for _ in range(k):
    a,b = map(int,input().split())
    arr[a][b] = 1

visited = [[0]*(m+1) for _ in range(n+1)]
result_arr = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 2

def bfs(x,y):
    result = 0
    queue = deque()
    queue.append((x,y))
    visited[x][y] = count
    result_arr.append(count)
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<1 or nx>=n+1 or ny<1 or ny>=m+1:
                continue
            
            if visited[nx][ny] == 0 and arr[nx][ny] == 1:
                visited[nx][ny] = count
                result_arr.append(count)
                queue.append((nx,ny))
                
    return result


for i in range(1,n+1):
    for j in range(1,m+1):
        if visited[i][j] == 0 and arr[i][j] == 1:
            answer = bfs(i,j)
            count+=1
            
# print(result_arr)
# print(arr)
# print(visited)
answer = Counter(result_arr)
# print(answer)
result = list(answer.values())
result.sort(reverse=True)
print(result[0])
