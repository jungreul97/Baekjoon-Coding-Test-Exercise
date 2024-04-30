import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())

arr = [[0]*N for _ in range(N)]

for _ in range(K):
    x,y = map(int,input().split())
    arr[x-1][y-1] = 1

commands = []
L = int(input())

for _ in range(L):
    t,c = map(str,input().split())
    commands.append((int(t),c))
commands.sort(reverse = True)
sec,cmd = commands.pop()


x,y = 0,0
time = 0
direction = 'R'
body = deque()
body.appendleft((x,y))
while True:
    time += 1
    #방향에 따라 머리 먼저 보내기
    if direction == 'R': y+=1
    elif direction == 'D': x+=1
    elif direction == 'L': y-=1
    else : x-=1
    #머리가 일단 사각형 밖으로 나가면 멈춤
    if x<0 or x>=N or y<0 or y>=N : break
    if (x,y) in body : break

    #사과 있는지 없는지 체크
    #있을 때 해당부분 사과 먹고 몸 리스트 한칸 앞으로만 가기
    if arr[x][y] == 1:
        arr[x][y] = 0
        body.appendleft((x,y))
    else:
        body.appendleft((x,y))
        body.pop()
    
    #시간에 따라 방향 바꾸기
    if time == sec:
        if cmd == 'L':
            if direction == 'R' : direction = 'U'
            elif direction == 'D' : direction = 'R'
            elif direction == 'L' : direction = 'D'
            else : direction = 'L'
        else:
            if direction == 'R' : direction = 'D'
            elif direction == 'D' : direction = 'L'
            elif direction == 'L' : direction = 'U'
            else : direction = 'R'
        if commands:
            sec,cmd = commands.pop()
        else:
            sec = 0
            cmd = ''

print(time)





