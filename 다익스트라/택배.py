import sys
import heapq
input = sys.stdin.readline()
INF = int(1e9)
n,m = map(int,input())
graph = [[] for i in range(n+1)]

for _ in range(m):
    start,end,d = map(int,input().split())
    graph[start].append([end,d])

result_arr = [[] for i in range(n+1)]

for i in range(n+1):
    dijkstra(i)

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            print('-')
        else:
            print(result_arr[i][j])
    
def dijkstra(start):
    q= []
    heapq.heappush(q,(0,start))
    distance = [INF]*(n+1)
    distance[start] = 0
    while q:
        dist,now = q.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                
                heapq.heappush(q,(cost,i[0]))
