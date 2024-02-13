import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
graph.append(list(0*i for i in range(m)))
result = int(1e9)
queue = deque()
for i in range(m):
    queue.append((0,i,'start',graph[0][i]))
while queue:
    x,y,command,dist = queue.popleft()
    if x == n:
        result = min(result,dist)
        continue
    if command == 'start': 
        if y-1>=0:
            queue.append((x+1,y-1,'left',dist+graph[x+1][y-1]))
        if y+1<m:
            queue.append((x+1,y+1,'right',dist+graph[x+1][y+1]))
        queue.append((x+1,y,'down',dist+graph[x+1][y]))
    elif command == 'left':
        if y+1<m:
            queue.append((x+1,y+1,'right',dist+graph[x+1][y+1]))
        queue.append((x+1,y,'down',dist+graph[x+1][y]))
    elif command == 'down':
        if y-1>=0:
            queue.append((x+1,y-1,'left',dist+graph[x+1][y-1]))
        if y+1<m:
            queue.append((x+1,y+1,'right',dist+graph[x+1][y+1]))
    elif command == 'right':
        if y-1>=0:
            queue.append((x+1,y-1,'left',dist+graph[x+1][y-1]))
        queue.append((x+1,y,'down',dist+graph[x+1][y]))
print(result)