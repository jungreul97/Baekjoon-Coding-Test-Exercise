def dfs(x,y):
    if visited[x][y] or arr[x][y] == 0:
        return 
    else:
        visited[x][y] = True
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            else:
                if not visited[nx][ny] and arr[nx][ny] == 1:
                    arr[nx][ny] += 1
                    dfs(nx,ny)  
    return

#상하좌우 대각선왼쪽위오른쪽위 대각선왼쪽아래 오른쪽아래
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,1,-1,-1,1,-1,1]

while True:
    m,n = map(int,input().split())
    if n == 0 and m == 0:
        break
    arr = []
    
    for i in range(n):
        arr.append(list(map(int,input().split())))
    
    if m == 1 and n == 1:
        if arr[0][0] == 0:
            print(0)
        else:
            print(1)
    
    else:
        visited = [[False for i in range(m)]for j in range(n)]

        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:#바다인곳 방문처리
                    visited[i][j] = True

        for i in range(n):
            for j in range(m):
                dfs(i,j)

        result = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1:
                    result+=1

        print(result)