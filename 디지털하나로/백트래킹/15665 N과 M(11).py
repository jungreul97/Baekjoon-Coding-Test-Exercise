import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = sorted(list(map(int,input().split())))

numbers = []

def dfs():
    if len(numbers) == M:
        print(*numbers)
        return
    check = 0
    for i in range(N):
        if arr[i] != check:
            numbers.append(arr[i])
            check = arr[i]
            dfs()
            numbers.pop()

dfs()