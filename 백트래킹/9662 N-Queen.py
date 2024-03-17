import sys
input = sys.stdin.readline

N = int(input())

visited = [[False]*N for _ in range(N)]
answer = 0
result = []
def dfs(cnt):
    global answer,result
    if cnt == N : 
        print(visited)
        if not visited in result:
            result.append(visited)
            answer += 1
        return
    
    for i in range(N):
        for j in range(N): 
            print(cnt,i,j)
            check = True
            if not visited[i][j]:
                tmp = 1
                while 0<=i-tmp:
                    if visited[i-tmp][j]: 
                        check = False
                        break
                    tmp+=1
                if not check : break
                tmp = 1
                while i+tmp<N:
                    if visited[i+tmp][j] : 
                        check = False
                        break
                    tmp+=1
                if not check : break
                tmp = 1
                while 0<=j-tmp:
                    if visited[i][j-tmp]: 
                        check = False
                        break
                    tmp+=1
                if not check : break
                tmp = 1
                while j+tmp<N:
                    if visited[i][j+tmp] : 
                        check = False
                        break
                    tmp+=1
                if not check : break
                tmp = 1
                while i+tmp<N and j+tmp<N:
                    if visited[i+tmp][j+tmp] : 
                        check = False
                        break
                    tmp+=1
                if not check : break
                tmp = 1
                while i+tmp<N and 0<=j-tmp:
                    if visited[i+tmp][j-tmp] : 
                        check = False
                        break
                    tmp+=1
                if not check : break
                tmp = 1
                while 0<=i-tmp and j+tmp<N:
                    if visited[i-tmp][j+tmp] : 
                        check = False
                        break
                    tmp+=1
                if not check : break
                tmp = 1
                while 0<=i-tmp and 0<=j-tmp:
                    if visited[i-tmp][j-tmp] : 
                        check = False
                        break
                    tmp+=1
                if not check : break

                visited[i][j] = True
                dfs(cnt+1)
                visited[i][j] = False

dfs(0)
print(answer)