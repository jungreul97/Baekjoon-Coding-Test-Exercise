import sys
from collections import deque
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()
queue = deque()
queue.append(t)
while queue:
    now = queue.popleft()
    if len(now) == len(s):
        if now == s:
            print(1)
            exit()
        continue
    if now[0] == 'B':
        queue.append(now[1:][::-1])
    if now[-1] == 'A':
        queue.append(now[:-1])
print(0)

# 메모리 초과난 풀이 s -> t로 만들기
# queue = deque()
# queue.append(s)
# while queue:
#     # print(queue)
#     # print(arr)
#     now = queue.popleft()
#     if len(now) == len(t) :
#         if now == t : 
#             print(1)
#             exit()
#         continue
#     if not 'A'+now in arr:
#         arr.add(now+'A')
#         queue.append(now+'A')
#     if not (now+'B')[::-1] in arr:
#         arr.add((now+'B')[::-1])
#         queue.append((now+'B')[::-1]) #문자열 뒤집기
# print(0)

    

