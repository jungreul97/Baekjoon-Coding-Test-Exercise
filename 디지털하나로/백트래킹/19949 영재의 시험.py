import sys
from collections import deque
input = sys.stdin.readline

arr = list(map(int,input().split()))
nums = []
cnt = 0

def dfs(idx):
    global cnt
    if idx == 10 :
        po = 0
        for i in range(10):
            if nums[i] == arr[i]: po +=1
        if po >= 5: cnt+=1
        return
    for i in range(1,6):
        if idx>=2 and nums[idx-2] == nums[idx-1] == i:
            continue
        nums.append(i)
        if i == arr[idx]:
            dfs(idx+1)
        else:
            dfs(idx+1)
        nums.pop()

dfs(0)
print(cnt)

