import sys
input = sys.stdin.readline
from collections import deque

arr = [] # 수열 받는 리스트
stack = [] # 스택
cmd = [] # 결과물
n = int(input())
queue = deque()

for i in range(1,n+1):
    queue.append(i)
for _ in range(n):
    number = int(input())
    arr.append(number)
check = True

for i in range(arr):
    target = i
    if not stack or queue[0]<=target:
        stack.append(queue.popleft())
        cmd.append("+")
    if stack[-1] == target:
        stack.pop()
        cmd.append("-")
    else:
        check = False
        break


if check:
    for i in cmd:
        print(i)
else:
    print("NO")

# for i in arr:
#     target = i
#     if not stack or stack[-1] < target:
#         while queue and queue[0] <= target:
#             stack.append(queue.popleft())
#             cmd.append("+")
#     if stack[-1] == target:
#         stack.pop()
#         cmd.append("-")
#     else:
#         check = False
#         break