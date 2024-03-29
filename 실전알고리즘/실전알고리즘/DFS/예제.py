# def dfs(graph,v,visited):
#     if not visited[v]:
#         visited[v] = True
#         print(v,end=" ")
#         for i in graph[v]:
#             if not visited[i]:
#              dfs(graph,i,visited)

def dfs(graph,v,visited):
    if not visited[v]:
        visited[v] = True
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                dfs(graph,i,visited)

graph = [
    [], #인덱스0에 대해서 비워두자
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

dfs(graph,1,visited)