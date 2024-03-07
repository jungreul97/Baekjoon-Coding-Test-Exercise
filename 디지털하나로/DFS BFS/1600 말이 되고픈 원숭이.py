import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
M,N = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
hx = [-2, -1, 1, 2, 2, 1, -1, -2]
hy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(): # 도착하지 않은 경우에 -1 같은거를 반환하는 문제는 함수를 만들어서 풀어버리자 정률아!!
    queue = deque()
    visited = [[[False] * (k+1) for _ in range(M)] for _ in range(N)]
    visited[0][0][k] = True
    queue.append((0,0,k,0))

    while queue:
        x,y,pos,cnt = queue.popleft()
        if x == N-1 and y == M-1:
            return cnt
        if pos > 0:
            for i in range(8):
                nx,ny = x+hx[i],y+hy[i]
                if 0<=nx<N and 0<=ny<M:
                    if not visited[nx][ny][pos-1] and graph[nx][ny] == 0:
                        visited[nx][ny][pos-1] = True
                        queue.append((nx,ny,pos-1,cnt+1))

        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<M:
                if not visited[nx][ny][pos] and graph[nx][ny] == 0:
                    visited[nx][ny][pos] = True
                    queue.append((nx,ny,pos,cnt+1))
    return -1

print(bfs())


