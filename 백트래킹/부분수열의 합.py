import sys
input = sys.stdin.readline

N,S = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
nums = []

def dfs(start):
    global cnt
    if sum(nums) == S and len(nums) > 0:
        # print(nums)
        cnt+=1
        
    for i in range(start,N):
        nums.append(arr[i])
        dfs(i+1)
        nums.pop()
dfs(0)
print(cnt)