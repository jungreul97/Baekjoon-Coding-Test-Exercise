import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())

max_num = -1e9
min_num = 1e9

def dfs(i,result):
    global add,sub,mul,div,max_num,min_num
    if i == n:
        max_num = max(max_num,result)
        min_num = min(min_num,result)
        return
    if add>0:
        add-=1
        dfs(i+1,result+arr[i])
        add+=1
    if sub>0:
        sub-=1
        dfs(i+1,result-arr[i])
        sub+=1
    if mul>0:
        mul-=1
        dfs(i+1,result*arr[i])
        mul+=1
    if div>0:
        div-=1
        dfs(i+1,int(result/arr[i]))
        div+=1
    
dfs(1,arr[0])
print(max_num)
print(min_num)
