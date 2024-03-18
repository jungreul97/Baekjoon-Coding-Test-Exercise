import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int,input().split()))

arr = [False]*(sum(S)+1)
visited = [False]*N

def dfs(start,sum):
    global arr
    if start == N: return
    
    if not visited[start]:
        arr[sum+S[start]] = True
        visited[start] = True
        dfs(start+1,sum+S[start])
        visited[start] = False
        dfs(start+1,sum)

dfs(0,0)
answer = 0
for i in range(1,len(arr)):
    if not arr[i] : 
        answer = i
        break
# print(arr)
if answer == 0: print(len(arr))
else : print(answer)