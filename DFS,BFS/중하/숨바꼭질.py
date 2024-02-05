import sys
from collections import deque
def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        if v == k:
            return
        elif v>k:
            if visited[v-1] == 0 or visited[v-1]>visited[v]+1:
                visited[v-1] = visited[v]+1
                queue.append(v-1)
        else:
            if v-1>=1 and (visited[v-1] == 0 or visited[v-1]>visited[v]+1):
                visited[v-1] = visited[v]+1
                queue.append(v-1)
            if v+1<100001 and (visited[v+1] == 0 or visited[v+1]>visited[v]+1):
                visited[v+1] = visited[v]+1
                queue.append(v+1)
            if v*2 < 100001 and (visited[v*2] == 0 or visited[v*2]>visited[v]+1):
                visited[v*2] = visited[v]+1
                queue.append(v*2)

n,k = map(int,sys.stdin.readline().split())
visited = [0]*(1000001)
bfs(n)
# for i in range(1,k+3):
#     print(visited[i],end=' ')
 
print(visited[k])
