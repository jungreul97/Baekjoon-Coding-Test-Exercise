import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
queue = deque()
cnt = 0
answer = []
for i in range(1,n+1):
    queue.append(i)
while queue:
    x = queue.popleft()
    if len(queue) == 0:
        answer.append(x)
        break
    cnt+=1
    if cnt != k:
        queue.append(x)
    else:
        answer.append(x)
        cnt = 0
s = ''
for i in answer:
    s+=" "+str(i)+","

s= s.lstrip()
s = "<"+''.join(s[:-1])+">"

print(s)