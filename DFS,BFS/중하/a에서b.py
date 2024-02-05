import sys
from collections import deque
def bfs(v):
    queue = deque()
    queue.append((v,1))
    while queue:
        v,count = queue.popleft()
        if v == b:
            return count
        else:
            nums = [v*2,v*10+1]
            for i in nums:
                if i<=b:
                    queue.append((i,count+1))
    return -1
a,b = map(int,sys.stdin.readline().split())


print(bfs(a))
     
    
        





# def dfs(v):
#     if v == b:
#         return
#     else:
#         s = str(v)
#         s = s+'1'
#         n = int(s)
#         if v*2<=b:
#             if visited[v*2] == 0:
#                 visited[v*2] = visited[v]+1
#                 dfs(v*2)
#         if n<=b: 
#             if visited[n] == 0:
#                 visited[n] = visited[v]+1
#                 dfs(n)