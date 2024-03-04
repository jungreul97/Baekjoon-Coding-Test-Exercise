import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
numbers = []

def dfs(start):
    if len(numbers) == M:
        print(*numbers,sep = " ")
        return
    for i in range(start,N):
        if not arr[i] in numbers:
            numbers.append(arr[i])
            dfs(i+1)
            numbers.pop()

dfs(0)
