import sys
input = sys.stdin.readline

def dfs(depth,idx):
    global min_diff
    if depth == n//2:
        start,link = 0,0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start+=arr[i][j]   
                elif not visited[i] and not visited[j]:
                    link+=arr[i][j]
                    
        min_diff = min(min_diff,abs(start-link))
        return
    
    for i in range(idx,n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1,i+1)
            visited[i] = False



n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().rstrip().split())))

min_diff = int(1e9)
visited = [False] * n

dfs(0,0)
print(min_diff)
