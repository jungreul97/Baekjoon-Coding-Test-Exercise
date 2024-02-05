import sys
input = sys.stdin.readline
from collections import deque

a,b = map(int,input().split())


def solve():
    queue = deque()
    queue.append((a,1)) 
    while queue:
        start,cnt = queue.popleft()
        if start == b:
            print(cnt)
            return
        if start*2<=b:
            queue.append((start*2,cnt+1))
        if start*10+1<=b:
            queue.append((start*10+1,cnt+1))
    print(-1)
    return

solve()