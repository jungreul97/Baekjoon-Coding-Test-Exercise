import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = sorted(list(map(int,input().split())))

visited = [False] * N
numbers = []
result = []


def dfs(start):
    global result
    if len(numbers) == M:
        print(*numbers)
        return
    check = 0
    for i in range(start,N):
        if not visited[i] and arr[i] != check:
            visited[i] = True
            numbers.append(arr[i])
            check = arr[i]
            dfs(i+1)
            numbers.pop()
            visited[i] = False


dfs(0)
