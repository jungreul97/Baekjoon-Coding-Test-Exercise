import sys,heapq
input = sys.stdin.readline

N,M,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))
# print(graph)

X_arrived = [int(1e9)]*(N+1) # X마을 도착 최소시간

for i in range(1,N+1):
    if i == X: continue
    q = []
    heapq.heappush(q,(0,i))
    i_arrived = [int(1e9)]*(N+1)
    while q:
        dist,now = heapq.heappop(q)
        # print(dist,now)
        if now == X: 
            X_arrived[i] = dist 
            break
        for j in graph[now]:
            cost = dist+j[1]
            if i_arrived[j[0]]>cost:
                i_arrived[j[0]] = cost
                heapq.heappush(q,(cost,j[0]))

My_arrived = [int(1e9)]*(N+1) # 자기 마을 도착 최소시간
q = []
heapq.heappush(q,(0,X))
while q:
    dist,now = heapq.heappop(q)
    for j in graph[now]:
        cost = dist+j[1]
        if My_arrived[j[0]]>cost:
            My_arrived[j[0]] = cost
            heapq.heappush(q,(cost,j[0]))

# print(X_arrived)
# print(My_arrived)

max_time = 0
for i in range(1,N+1):
    if i == X: continue
    max_time = max(max_time,X_arrived[i]+My_arrived[i])
print(max_time)
