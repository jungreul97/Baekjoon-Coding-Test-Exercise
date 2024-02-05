import sys
n,k = map(int,sys.stdin.readline().split())

arr = [[0]*(n+1)]
for _ in range(n):
    arr.append([0]+list(map(int,input().split())))

s,x,y = map(int,sys.stdin.readline().split())
# print(arr)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

time = [[0]*(n+1)for j in range(n+1)]
t=1
while t<=s:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i][j] == 0:
                result = float('inf')
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if nx<0 or nx>n or ny<0 or ny>n:
                        continue
                    else:
                        if time[nx][ny]<t and arr[nx][ny]!=0 and arr[nx][ny]<result:
                            result = arr[nx][ny]
                if result!=float('inf'):            
                    arr[i][j] = result
                    time[i][j] = t
    t+=1
    # print(arr)

print(arr[x][y])

                        
                            
