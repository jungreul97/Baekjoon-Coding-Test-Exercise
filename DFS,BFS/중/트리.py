import sys
from collections import deque
def bfs(v):
    global answer
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        for i in arr[v]:
            if len(arr[i]) == 0:
                answer+=1
            else:
                queue.append(i)
        for i in arr:
            if remove in i:
                i.remove(v)
        answer+=1
        arr[v] = []
answer = 0
n = int(sys.stdin.readline())
arr = [[] for i in range(n)]
number = 0
input = list(map(int,input().split()))
for i in input:
    if i == -1:
        number+=1
        continue
    else:
        arr[i].append(number)
    number+=1
remove = int(sys.stdin.readline())

# print(arr)
bfs(remove)
# print(answer)
# print(arr)

result = 0
for i in arr:
    if len(i) == 0:
        result+=1
print(result-answer)
