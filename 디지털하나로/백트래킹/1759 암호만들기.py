import sys
input = sys.stdin.readline

L,C = map(int,input().split())
arr = list(map(str,input().split()))

arr.sort()
chars = []
moum = ['a','e','i','o','u']
print(arr)
def dfs(start,mon,jan):
    if len(chars) == L:
        if mon >= 1 and jan >= 2:
            print(''.join(chars))
        return
    
    for i in range(start,C):
        if not arr[i] in chars:
            chars.append(arr[i])
            if arr[i] in moum:
                dfs(i+1,mon+1,jan)
            else:
                dfs(i+1,mon,jan+1)
            chars.pop()

dfs(0,0,0)
