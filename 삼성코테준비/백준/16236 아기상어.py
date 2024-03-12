import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
water = []
start_x,start_y = 0,0
check = False
for i in range(N):
    arr = list(map(int,input().split()))
    water.append(arr)
    if check : continue
    for j in range(N):
        if arr[j] == 9: 
            start_x,start_y = i,j
            check = True
            break
dx = [-1,1,0,0]
dy = [0,0,-1,1]
baby = 2 # 초기 아기 상어 크기
eat_cnt = 0 # 상어가 먹은 물고기 수
time = 0
possible_eat = []
water[start_x][start_y] = 0

def bfs(start_x,start_y):
    queue = deque()
    queue.append((start_x,start_y,0))
    visited = [[False]*N for _ in range(N)]
    visited[start_x][start_y] = True
    min_dist = int(1e9)
    while queue:
        x,y,cnt = queue.popleft()
        if cnt > min_dist : continue # 현재 최소거리 보다 멀면 패스
        if water[x][y] != 0 and water[x][y] < baby and cnt<=min_dist : # 해당 자리의 물고기의 크기가 아기상어의 크기보다 작다면
            if cnt<min_dist : 
                min_dist = cnt
                possible_eat.clear()
            possible_eat.append((x,y,cnt))
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and water[nx][ny] <= baby:
                visited[nx][ny] = True
                queue.append((nx,ny,cnt+1))
    # print(start_x,start_y)
    if possible_eat: eat()
    else : return

def eat():
    global eat_cnt,baby,time
    possible_eat.sort(key = lambda x : (x[0],x[1]))
    # print(possible_eat)
    start_x,start_y,cnt = possible_eat[0][0],possible_eat[0][1],possible_eat[0][2] # 탐색할 인덱스 초기화
    water[start_x][start_y] = 0 # 해당 자리 물고기 먹힘
    eat_cnt += 1 #  먹은 물고기 수 증가
    if eat_cnt == baby: # 먹은 물고기 수가 상어의 크기와 같다면
        baby+=1
        eat_cnt = 0
    time += cnt
    # print(time)
    possible_eat.clear()
    bfs(start_x,start_y)


bfs(start_x,start_y)

print(time)