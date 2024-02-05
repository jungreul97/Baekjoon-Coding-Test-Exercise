import sys
input = sys.stdin.readline

def bfs(cmd,x,y):
    visited[x][y] = True
    if cmd == 1:
        cases = []
        result = 0
        #위
        for i in range(x-1,-1,-1):
            if arr[i][y] == 6:
                break
            if not visited[i][y]:
                result+=1
        cases.append((result,1))
        result = 0
        #우
        for i in range(y+1,m):
            if arr[x][i] == 6:
                break
            if not visited[x][i]:
                result+=1
        cases.append((result,2))
        result = 0
        #아래
        for i in range(x+1,n):
            if arr[i][y] == 6:
                break
            if not visited[i][y]:
                result+=1
        cases.append((result,3))
        result = 0
        #좌
        for i in range(y-1,-1,-1):
            if arr[x][i] == 6:break
            if not visited[x][i]:
                result+=1
        cases.append((result,4))

        cases.sort(reverse = True)
        if cases[0][1] == 1:
            #위
            for i in range(x-1,-1,-1):
                if arr[i][y] == 6:break
                visited[i][y] = True
        elif cases[0][1] == 2:
            #우
            for i in range(y+1,m):
                if arr[x][i] == 6:break
                visited[x][i] = True
        elif cases[0][1] == 3:
            #아래
            for i in range(x+1,n):
                if arr[i][y] == 6:break
                visited[i][y] = True
        else:
            #좌
            for i in range(y-1,-1,-1):
                if arr[x][i] == 6:break
                visited[x][i] = True
        
    elif cmd == 2:
        cases = []
        result = 0
        #좌
        for i in range(y-1,-1,-1):
            if arr[x][i] == 6:break
            if not visited[x][i]:
                result+=1
        #우
        for i in range(y+1,m):
            if arr[x][i] == 6:break
            if not visited[x][i]:
                result+=1
        cases.append((result,1))
        result = 0
        #위
        for i in range(x-1,-1,-1):
            if arr[i][y] == 6:break
            if not visited[i][y]:
                result+=1
        #아래
        for i in range(x+1,n):
            if arr[i][y] == 6:break
            if not visited[i][y]:
                result+=1
        cases.append((result,2))
        
        cases.sort(reverse = True)
        if cases[0][1] == 1:
            #좌
            for i in range(y-1,-1,-1):
                if arr[x][i] == 6:break
                visited[x][i] = True
            #우
            for i in range(y+1,m):
                if arr[x][i] == 6:break
                visited[x][i] = True
        else:
            #위
            for i in range(x-1,-1,-1):
                if arr[i][y] == 6:break
                visited[i][y] = True
            #아래
            for i in range(x+1,n):
                if arr[i][y] == 6:break
                visited[i][y] = True
            
    elif cmd == 3:
        cases = []
        result = 0
        #위
        for i in range(x-1,-1,-1):
            if arr[i][y] == 6:break
            if not visited[i][y]:
                result+=1
        #우
        for i in range(y+1,m):
            if arr[x][i] == 6:break
            if not visited[x][i]:
                result+=1
        cases.append((result,1))

        result = 0
        #우
        for i in range(y+1,m):
            if arr[x][i] == 6:break
            if not visited[x][i]:
                result+=1
        #아래
        for i in range(x+1,n):
            if arr[i][y] == 6:break
            if not visited[i][y]:
                result+=1
        cases.append((result,2))

        result = 0
        #아래
        for i in range(x+1,n):
            if arr[i][y] == 6:break
            if not visited[i][y]:
                result+=1
        #좌
        for i in range(y-1,-1,-1):
            if arr[x][i] == 6:break
            if not visited[x][i]:
                result+=1
        cases.append((result,3))

        result = 0
        #좌
        for i in range(y-1,-1,-1):
            if arr[x][i] == 6:break
            if not visited[x][i]:
                result+=1
        #위
        for i in range(x-1,-1,-1):
            if arr[i][y] == 6:break
            if not visited[i][y]:
                result+=1
        cases.append((result,4))

        cases.sort(reverse = True)
        if cases[0][1] == 1:
            #위
            for i in range(x-1,-1,-1):
                if arr[i][y] == 6:break
                visited[i][y] = True
            #우
            for i in range(y+1,m):
                if arr[x][i] == 6:break
                visited[x][i] = True
        elif cases[0][1] == 2:
            #우
            for i in range(y+1,m):
                if arr[x][i] == 6:break
                visited[x][i] = True
            #아래
            for i in range(x+1,n):
                if arr[i][y] == 6:break
                visited[i][y] = True
        elif cases[0][1] == 3:
            #아래
            for i in range(x+1,n):
                if arr[i][y] == 6:break
                visited[i][y] = True
            #좌
            for i in range(y-1,-1,-1):
                if arr[x][i] == 6:break
                visited[x][i] = True
        else:
            #좌
            for i in range(y-1,-1,-1):
                if arr[x][i] == 6:break
                visited[x][i] = True
            #위
            for i in range(x-1,-1,-1):
                if arr[i][y] == 6:break
                visited[i][y] = True

    elif cmd == 4:
        cases = []
        result = 0
        #좌
        for i in range(y-1,-1,-1):
            if arr[x][i] == 6:break
            if not visited[x][i]:
                result+=1
        #위
        for i in range(x-1,-1,-1):
            if arr[i][y] == 6:break
            if not visited[i][y]:
                result+=1
        #우
        for i in range(y+1,m):
            if arr[x][i] == 6:break
            if not visited[x][i]:
                result+=1
        cases.append((result,1))

        result = 0
        #위
        for i in range(x-1,-1,-1):
            if arr[i][y] == 6:break
            if not visited[i][y]:
                result+=1
        #우
        for i in range(y+1,m):
            if arr[x][i] == 6:break
            if not visited[x][i]:
                result+=1
        #아래
        for i in range(x+1,n):
            if arr[i][y] == 6:break
            if not visited[i][y]:
                result+=1
        cases.append((result,2))

        result = 0
        #우
        for i in range(y+1,m):
            if arr[x][i] == 6:break
            if not visited[x][i]:
                result+=1
        #아래
        for i in range(x+1,n):
            if arr[i][y] == 6:break
            if not visited[i][y]:
                result+=1
        #좌
        for i in range(y-1,-1,-1):
            if arr[x][i] == 6:break
            if not visited[x][i]:
                result+=1
        cases.append((result,3))

        result = 0
        #아래
        for i in range(x+1,n):
            if arr[i][y] == 6:break
            if not visited[i][y]:
                result+=1
        #좌
        for i in range(y-1,-1,-1):
            if arr[x][i] == 6:break
            if not visited[x][i]:
                result+=1
        #위
        for i in range(x-1,-1,-1):
            if arr[i][y] == 6:break
            if not visited[i][y]:
                result+=1
        cases.append((result,4))
        cases.sort(reverse = True)
        if cases[0][1] == 1:
            #좌
            for i in range(y-1,-1,-1):
                if arr[x][i] == 6:break
                visited[x][i] = True
            #위
            for i in range(x-1,-1,-1):
                if arr[i][y] == 6:break
                visited[i][y] = True
            #우
            for i in range(y+1,m):
                if arr[x][i] == 6:break
                visited[x][i] = True
        elif cases[0][1] == 2:
            #위
            for i in range(x-1,-1,-1):
                if arr[i][y] == 6:break
                visited[i][y] = True
            #우
            for i in range(y+1,m):
                if arr[x][i] == 6:break
                visited[x][i] = True
            #아래
            for i in range(x+1,n):
                if arr[i][y] == 6:break
                visited[i][y] = True
        elif cases[0][1] == 3:
            #우
            for i in range(y+1,m):
                if arr[x][i] == 6:break
                visited[x][i] = True
            #아래
            for i in range(x+1,n):
                if arr[i][y] == 6:break
                visited[i][y] = True
            #좌
            for i in range(y-1,-1,-1):
                if arr[x][i] == 6:break
                visited[x][i] = True
        else:
            #아래
            for i in range(x+1,n):
                if arr[i][y] == 6:break
                visited[i][y] = True
            #좌
            for i in range(y-1,-1,-1):
                if arr[x][i] == 6:break
                visited[x][i] = True
            #위
            for i in range(x-1,-1,-1):
                if arr[i][y] == 6:break
                visited[i][y] = True
    else:
        #위
        for i in range(x-1,-1,-1):
            if arr[i][y] == 6:break
            visited[i][y] = True
        #아래
        for i in range(x+1,n):
            if arr[i][y] == 6:break
            visited[i][y] = True
        #좌
        for i in range(y-1,-1,-1):
            if arr[x][i] == 6:break
            visited[x][i] = True
        #우
        for i in range(y+1,m):
            if arr[x][i] == 6:break
            visited[x][i] = True
        
    return

n,m = map(int,input().split())
arr = []
cctvs = []
for _ in range(n):
    arr.append(list(map(int,input().rstrip().split())))
visited = [[False]*(m) for _ in range(n)]
queue = []
answer = 0
for i in range(n):
    for j in range(m):
        if 1<=arr[i][j]<=5:
            cctvs.append((arr[i][j],i,j))
        elif arr[i][j] == 6:
            answer-=1

cctvs.sort(reverse = True)
for cctv in cctvs:
    bfs(cctv[0],cctv[1],cctv[2])

for i in visited:
    answer+=i.count(False)

for i in range(n) :   
    print(visited[i])

print(answer)

                    