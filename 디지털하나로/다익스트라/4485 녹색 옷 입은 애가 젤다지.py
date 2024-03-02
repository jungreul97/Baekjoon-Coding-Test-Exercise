import sys
import heapq
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,1,-1]
number = 1
while True:
    n = int(input())
    if n == 0:break
    graph = []
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    min_total = [[int(1e9)]*n for i in range(n)]
    max_num = int(1e9)
    q = []
    heapq.heappush(q,(graph[0][0],0,0))
    min_total[0][0] = graph[0][0]
    while q:
        money,x,y = heapq.heappop(q)
        if x == n-1 and y == n-1: break
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:continue
            cost = money+graph[nx][ny]
            if min_total[nx][ny]>cost:
                min_total[nx][ny] = cost
                heapq.heappush(q,(cost,nx,ny))
    # for i in range(n):
    #     print(*min_total[i])
    print("Problem {}: {}".format(number,min_total[n-1][n-1]))
    number+=1
