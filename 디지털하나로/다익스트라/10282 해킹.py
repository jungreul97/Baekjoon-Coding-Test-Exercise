import sys, heapq
input = sys.stdin.readline
inf = int(1e9)

def dijkstra(graph,start):
    total = [inf]*(n+1)
    total[start] = 0  

    answer, maxtime = 0, 0

    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist,now = heapq.heappop(q)
        if dist<total[now] : continue # 이미값이 갱신되었는데 거기에 원래 더 오랜 감염시간이 걸리는 컴퓨터가 있다면 갱신하면 넘어가

        for i in graph[now]:
            if total[i[0]]<=dist + i[1]: continue # 같을때도 걍 넘겨 @@@@ㄹㅇ 중요!!!!!!!!!! 
            total[i[0]] = dist + i[1]
            heapq.heappush(q,(dist + i[1],i[0]))

    for t in total:
        if t<inf:
            answer+=1
            maxtime = max(maxtime,t)

    return answer,maxtime

T = int(input())
for _ in range(T):
    n,d,c = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a,b,cost = map(int,input().split())
        graph[b].append((a,cost))
    # print("🚀 ~ graph:", graph)
    answer,maxtime = dijkstra(graph,c)
    print(answer,maxtime)

