# from collections import deque

# def dfs(arr,v,visited):
#     if not visited[v]:
#         visited[v] = True
#         print(v,end= ' ')
#         index = []
#         for i in range(1,m+1):
#             if arr[i][0] == v or arr[i][1] == v:
#                 if arr[i][0] == v:
#                     if not visited[arr[i][1]]:
#                         index.append(arr[i][1])
#                 else:
#                     if not visited[arr[i][0]]:
#                         index.append(arr[i][0])
#         index.sort()
#         for i in range(len(index)):
#             dfs(arr,index[i],visited1)

# def bfs(arr,v,visited):
#     queue = deque([v])
#     while queue:
#         start = queue.popleft()
#         if not visited[start]:
#             visited[start] = True
#             print(start,end = ' ')
#             index = []
#             for i in range(1,m+1):
#                 if arr[i][0] == start or arr[i][1] == start:
#                     if not visited[arr[i][1]]:
#                         index.append(arr[i][1])
#                     elif not visited[arr[i][0]]:
#                         index.append(arr[i][0])
#             index.sort()
#             #낮은 숫자부터 탐색해야 하므로 인접한 노드중 낮은 순서대로 queue넣기
#             for i in range(len(index)):
#                 queue.append(index[i])

# n,m,v = map(int,input().split())
# arr = []

# for i in range(m):
#    arr.append(list(map(int,input().split())))
# arr = [[0,0]]+arr
# arr.sort()

# visited1 = [False] * (n+1)
# visited2 = [False] * (n+1)

# dfs(arr,v,visited1)
# print()
# bfs(arr,v,visited2)

import sys
input = sys.stdin.readline

def dfs(start):
    
    print(start,end = ' ')
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
    

n,m,start = map(int,input().split())
graph = [[]*n for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(n+1)
dfs(start)
