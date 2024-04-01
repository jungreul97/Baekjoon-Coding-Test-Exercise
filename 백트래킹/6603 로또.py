import sys
input = sys.stdin.readline

def dfs(start):
    if len(numbers) == 6:
        print(*numbers)
        return
    for i in range(start,k):
        numbers.append(arr[i])
        dfs(i+1)
        numbers.pop()

while True:
    li = list(map(int,input().split()))
    if li[0] == 0: break
    k = li[0]
    arr = li[1:]
    arr.sort()
    numbers = []
    dfs(0)
    print()
