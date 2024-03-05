import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())

max_answer = -int(1e9)
min_answer = int(1e9)

def dfs(num,idx,add,sub,mul,div):
    global max_answer,min_answer
    if idx == N:
        max_answer = max(max_answer,num)
        min_answer = min(min_answer,num)
        return
    if add>0:
        dfs(num+arr[idx],idx+1,add-1,sub,mul,div)
    if sub>0:
        dfs(num-arr[idx],idx+1,add,sub-1,mul,div)
    if mul>0:
        dfs(num*arr[idx],idx+1,add,sub,mul-1,div)
    if div>0:
        dfs(int(num/arr[idx]),idx+1,add,sub,mul,div-1)
            

dfs(arr[0],1,add,sub,mul,div)

print(max_answer)
print(min_answer)


