import sys
input  = sys.stdin.readline

N,M = map(int,input().split())
depth = M

numbers = []
visited = [False] * (N+1)
arr = list(map(int,input().split()))
arr.sort()

def dfs():
    if len(numbers) == M:
        print(*numbers,sep=" ")
        return
    for i in range(N):
        if not arr[i] in numbers:
            numbers.append(arr[i])
            dfs()
            numbers.pop()
dfs()
