import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = [1,2,3]
result = []

def dfs(numbers):
    if sum(numbers) >= n:
        if sum(numbers) == n:
            # print(numbers)
            s = '+'.join(map(str,numbers))
            if not s in result:
                result.append(s)
                # print(result)
        return
    for i in range(3):
        numbers.append(arr[i])
        dfs(numbers)
        numbers.pop()

dfs([])
# print(result)
if len(result) < k:
    print(-1)
else:
    print(result[k-1])
