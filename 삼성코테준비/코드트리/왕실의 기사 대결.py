import sys
input = sys.stdin.readline

L,N,Q = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
knight = []
for _ in range(L):
    knight.append(list(map(int,input().split())))
command = []
for _ in range(Q):
    command.append(list(map(int,input().split())))
print(arr)
#기사 움직이는 함수
def move_up(kinght_number):
    return

def move_right(kinght_number):
    return

def move_down(kinght_number):
    
    return

def move_left(kinght_number):
    return

for i in command:
    if i[1] == 0: move_up(i[0])
    elif i[1] == 1 : move_right(i[0])
    elif i[1] == 2 : move_down(i[0])
    else : move_left(i[0])