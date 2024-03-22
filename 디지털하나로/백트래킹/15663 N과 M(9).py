import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
numbers = []
visited = [False] * N
def dfs():
    if len(numbers) == M:
        print(*numbers)
        return
    check = 0
    for i in range(N):
        if not visited[i] and check != arr[i]:
            check = arr[i]
            numbers.append(arr[i])
            visited[i] = True
            dfs()
            visited[i] = False
            numbers.pop()
dfs()
