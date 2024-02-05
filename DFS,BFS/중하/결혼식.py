import sys
from collections import deque
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

arr = [[] for _ in range(n+1)]
arr[0] = [0,0]
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

# print(arr)

visited = [0] * (n+1)

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        for i in arr[v]:
            if visited[i] == 0 and i != 1:
                visited[i] = visited[v]+1
                if visited[v]+1>=3:
                    return
                else:
                    queue.append(i)
bfs(1)
# print(visited)
result = 0
for i in visited:
    if i == 1 or i == 2:
        result+=1

print(result)


