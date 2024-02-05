from collections import deque

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start]= True
    while queue:#큐가 비어있지 않다면
        v = queue.popleft()
        print(v,end=' ') #큐에 넣어진 것들 모두 출력
        for i in graph[v]:
            if not visited[i]:#방문을 안했으면 방문처리
                queue.append(i)#해당 노드와 인접한 노드들을 큐에 넣고 넣기만 하고 출력은 안함
                visited[i] = True#해당 인덱스 방문 처리


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9
bfs(graph,1,visited)