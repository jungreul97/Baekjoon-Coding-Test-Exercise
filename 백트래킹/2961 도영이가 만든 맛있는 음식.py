import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

sin = 1
ssn = 0
answer = int(1e9)

def dfs(start,sin,ssn,cnt):
    global answer
    # print(sin,ssn)
    if 0 < cnt <= N: answer = min(answer,abs(sin-ssn))
    if cnt == N or answer == 0: return
    for i in range(start,N):
        if not visited[i]:
            visited[i] = True
            dfs(start+1,sin*arr[i][0],ssn+arr[i][1],cnt+1)
            visited[i] = False
visited = [False]*N
dfs(0,sin,ssn,0)
print(answer)