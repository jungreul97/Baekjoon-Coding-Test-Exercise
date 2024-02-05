import sys
from collections import deque
sys.setrecursionlimit(10**2)
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y  = queue.popleft()
        for i in range(1,n+2):
            if not visited[i]:
                if abs(arr[n+1][0]-x)+abs(arr[n+1][1]-y)<=1000:
                    return "happy"
                elif abs(arr[i][0]-x)+abs(arr[i][1]-y)<=1000:
                    queue.append((arr[i][0],arr[i][1]))
                    visited[i] = True
                    # print(queue)
                    # print(i,x,y)
                    # print("queue 넣는거",arr[i][0],arr[i][1])
                    
    return "sad"
    

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = []
    for _ in range(n+2):
        arr.append(list(map(int,input().split())))
    visited = [False] * (n+2)
    visited[0] = True
    # print(arr)
    print(bfs(arr[0][0],arr[0][1]))
    # print(visited)