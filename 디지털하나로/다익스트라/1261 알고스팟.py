import sys
import heapq
input = sys.stdin.readline

M,N = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().rstrip()))) # 연속된 숫자 배열로 받을 때 split 사용 안하는거 유의하자!
total = [[int(1e9)]*M for _ in range(N)]
total[0][0] = 0
# print(graph)
dx  = [-1,1,0,0]
dy  = [0,0,-1,1]

q = []
heapq.heappush(q,(0,0,0))
while q:
    cost,x,y = heapq.heappop(q)
    if x == N-1 and y == M-1 : break # 최소의 벽갯수가 항상 먼저 오니까
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=M: continue
        # print(nx,ny)
        if graph[nx][ny] == 0 and total[nx][ny] > cost:
            total[nx][ny] = cost
            heapq.heappush(q,(cost,nx,ny))
        elif graph[nx][ny] == 1 and total[nx][ny] > cost +1:
            total[nx][ny] = cost+1
            heapq.heappush(q,(cost+1,nx,ny))
print(total[N-1][M-1])
            



