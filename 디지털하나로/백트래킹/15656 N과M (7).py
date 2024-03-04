import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
numbers = []

def dfs():
    if len(numbers) == M:
        print(*numbers,sep = " ")
        return
    for i in range(N):
        numbers.append(arr[i])
        dfs()
        numbers.pop()

dfs()
