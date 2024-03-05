import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
numbers = []

def dfs(start):
    if len(numbers) == M:
        print(*numbers)
        return
    for i in range(start,N):
        numbers.append(arr[i])
        dfs(i)
        numbers.pop()

dfs(0)