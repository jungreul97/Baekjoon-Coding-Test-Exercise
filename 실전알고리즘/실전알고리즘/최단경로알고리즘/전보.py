import sys
import heapq
n,m,start = map(int,sys.stdin.readline().split())
INF = int(1e9)
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    

dijkstra(start)
print(distance)

count = 0
max_distance = 0

for i in distance:
    if i == 0 or i == INF:
        continue
    else:
        count+=1
        if max_distance<i:
            max_distance = i
print(count,max_distance)
