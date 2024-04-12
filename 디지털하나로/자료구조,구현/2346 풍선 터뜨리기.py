import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

queue = deque()
for i in range(1,N):
    queue.append(i)
result = [1]

while queue:
    num = arr[result[-1]-1]
    if num > 0:
        for _ in range(num-1):
            x = queue.popleft()
            queue.append(x)
        x = queue.popleft()
        result.append(x+1)
    else : 
        num = -1 * num
        for _ in range(num-1):
            x = queue.pop()
            queue.appendleft(x)
        x = queue.pop()
        result.append(x+1)
   
print(*result)
