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
    check = 0
    for i in range(start,N):
        if arr[i] != check:
            numbers.append(arr[i])
            check = arr[i]
            dfs(i)
            numbers.pop()

dfs(0)




# def dfs(start):
#     if len(numbers) == M:
#         print(*numbers)
#         return
#     check = 0
#     for i in range(start,len(arr)):
#         if arr[i] != check:
#             numbers.append(arr[i])
#             check = arr[i]
#             dfs(i)
#             numbers.pop()

#     return 

# dfs(0)