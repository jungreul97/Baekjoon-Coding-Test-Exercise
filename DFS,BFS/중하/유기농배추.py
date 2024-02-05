import sys
sys.setrecursionlimit(10 ** 4)
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
       return False
   
    else:
        if arr[x][y] == 1:
            arr[x][y] = 0
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            return True
    return False

t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    arr = [[0 for i in range(m)] for j in range(n)]
    for i in range(k):
        x,y = map(int,input().split())
        arr[x][y] = 1

    result = 0
    for j in range(n):
        for l in range(m):
            if dfs(j,l) == True:
                result+=1
    
    print(result)