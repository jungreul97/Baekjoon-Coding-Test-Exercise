import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().split())
start = int(input())
INF = int(1e9)
distance = [INF]*(n+1)
graph = [[]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

q = []
#시작하고자 하는 노드의 거리는 0
distance[start] = 0
heapq.heappush(q,(0,start))
while q:
    dist,now = heapq.heappop(q)
    #거리의 값이 현재 거리보다 적으면 그냥 넘어감
    if distance[now]<dist:
        continue
    #현재 노드에서 갈수있는 짧은 노드부터 탐색
    for i in graph[now]:
        cost = dist+i[1] #짧은 노드부터 현재노드까지의 거리와 더함
        if cost<distance[i[0]]:
            distance[i[0]] = cost
            #넣을때는 비용이 앞으로 가게 힙이니까,그리고 목적지
            heapq.heappush(q,(cost,i[0]))

for i in distance:
    if i == INF:
        print("INF")
    else:
        print(i)

