def dfs(arr,x,visited):
    if not visited[x]:
        visited[x] = True
        for i in range(1,m+1):
            if arr[i][0] == x or arr[i][1] == x:
                if arr[i][0] == x:
                    if not visited[arr[i][1]]:
                        dfs(arr,arr[i][1],visited)
                else:
                    if not visited[arr[i][0]]:
                        dfs(arr,arr[i][0],visited)
        return True    
    return False


n,m = map(int,input().split())
visited = [False] * (n+1)

arr = []
arr.append([0,0])
result = 0

for i in range(m):
    arr.append(list(map(int,input().split())))
for i in range(1,n+1):
    if dfs(arr,i,visited):
        result+=1

print(result)
