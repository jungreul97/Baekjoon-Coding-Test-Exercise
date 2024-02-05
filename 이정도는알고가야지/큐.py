import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()
while n>0:
    cmd = sys.stdin.readline().strip()
    a = cmd.split()

    if a[0] == "push_front":
        queue.appendleft(a[1])
    elif a[0] == "push_back":
        queue.append(a[1])    
    elif a[0] == "pop_front":
        if len(queue)!=0:
            number = queue.popleft()
            print(number)
        else:
            print(-1)
    elif a[0] == "pop_back":
        if len(queue)!=0:
            number = queue.pop()
            print(number)
        else:
            print(-1)
    elif a[0] == "size":
        print(len(queue))
    elif a[0] == "empty":
        if len(queue)!=0:
            print(0)
        else:
            print(1)
    elif a[0] == "front":
        if len(queue)!=0:
            print(queue[0])
        else:
            print(-1)
    elif a[0] == "back":
        if len(queue)!=0:
            print(queue[-1])
        else:
            print(-1)

    n-=1
    