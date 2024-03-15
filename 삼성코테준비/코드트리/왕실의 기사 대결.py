import sys
from collections import deque
input = sys.stdin.readline

def move_knight(knight_number,cmd):
    x_move,y_move = dx[cmd],dy[cmd]
    now_knight = find_kinght(knight_number)
    print(now_knight)
    return

def find_kinght(knight_number):
    now_knight = []
    for i in range(1,L+1):
        for j in range(1,L+1):
            if knight_arr[i][j] == knight_number:
                now_knight.append((i,j))
    return now_knight

def move_check():
    return


L,N,Q = map(int,input().split())
arr = [[0]*(L+1)]
for _ in range(L):
    arr.append([0]+list(map(int,input().split())))
knights = []
for _ in range(N):
    knights.append(list(map(int,input().split())))
commands = []
for _ in range(Q):
    commands.append(list(map(int,input().split())))
knight_arr = [[0]*(L+1) for _ in range(L+1)]
knight_hp = [0,0,0] # 앞에 index 3 부터 나이트 번호 들어옴
knight_num = 3
for k in knights:
    x,y,h,w,hp = k[0],k[1],k[2],k[3],k[4]
    tmp_x,tmp_y = x,y
    while h>0:
        knight_arr[tmp_x][y] = knight_num
        tmp_x+=1
        h-=1
    while w>0:
        knight_arr[x][tmp_y] = knight_num
        tmp_y+=1
        w-=1
    knight_hp.append(hp)
    knight_num+=1

for i in range(L+1):
    print(*knight_arr[i])
print(knight_hp)

# 상,우,하,좌
dx = [0,-1,0,1,0]
dy = [0,0,1,0,-1]

for command in commands:
    knight_number,cmd = command[0]+2,command[1]
    move_knight(knight_number,cmd)



#정답출력
print(sum(knight_hp))


