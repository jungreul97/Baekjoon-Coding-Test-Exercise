import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split())
arr = []
virus = []
for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(N):
        if tmp[j] == 2: virus.append((i,j))
    arr.append(tmp)

cases = list(combinations(virus,M)) # 중복을 제외한 바이러스 선택하는 경우의 수 구하기
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 덱큐를 이용한 풀이 : 모든 케이스 마다 끝까지 타고 들어가서 갱신하고 바이러스마다 거리 이동해서 최소거리일때만 갱신화
def bfs(case):
    global answer
    queue = deque() 
    visited = [[int(1e9)]*N for _ in range(N)]
    for i in range(M): 
        queue.append((case[i][0],case[i][1],0)) # 바이러스 케이스마다 덱큐 투입 (바이러스 x좌표, 바이러스 y좌표, 초기거리 : 0)
        visited[case[i][0]][case[i][1]] = 0 # 바이러스가 있던 곳은 0 처리
    while queue:
        x,y,dist = queue.popleft()
        if visited[x][y] < dist : continue # 갱신되어 있는데 지금의 거리보다 작으면 넘어가기
        if arr[x][y] == 2 and visited[x][y] != int(1e9) and visited[x][y] != 0 : visited[x][y] -= int(1e9) # 비활성화된 바이러스인데 바이러스가 왔다면 거리정보가 들어가게 되므로 원래 초기값으로 변경하기@@@@@!!!!!!!!!!!
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<N and arr[nx][ny] != 1  and dist+1<visited[nx][ny]: # 아직 갱신하지 않았거나 기존 시간보다 작다면
                visited[nx][ny] = dist+1
                queue.append((nx,ny,dist+1))
    # print(case)
    # for i in range(N):
    #     print(*visited[i])
    max_time = 0
    zero_check = False # 바이러스 확산 후 빈칸이 남아 있는지 체크
    for i in range(N):
        for j in range(N):
            if visited[i][j] == int(1e9) and arr[i][j] == 0 : # 기존에도 빈칸인데 visited도 갱신되지 않았다면 바이러스가 도달하지 못한것 -> 케이스에서 제외해야지
                zero_check = True 
                break
            if visited[i][j] != int(1e9) and visited[i][j] > max_time: max_time = visited[i][j]
        if zero_check : break
    if not zero_check: answer = min(answer,max_time)

answer = int(1e9) # case중 가장 오래 걸리는 시간중에 가장 최솟값을 구해야 하므로 최댓값으로 초기 설정
for case in cases : 
    bfs(case)

if answer == int(1e9) : print(-1) # 정답이 갱신되지 않았다면 모든 케이스에서 바이러스가 침투하지 못한것이므로 -1 출력
else: print(answer) # 정답이 갱신되었다면 최소 시간 출력


# 기존 heapq로 구현해서 해결한 풀이 -> deque 보다 heapq가 NlogN의 복잡도를 가지기에 더 오래걸릴 수 있어서 시간초과가 난듯하다.!!!!!! 열심히 풀었는데!!!!!
# def bfs(case):
#     global answer
#     q = [] # 시간이 적은 순부터 들어가게 하기 위한 힙큐
#     visited = [[int(1e9)]*N for _ in range(N)]
#     for i in range(M): 
#         heapq.heappush(q,(0,case[i][0],case[i][1])) # 바이러스 케이스마다 힙큐에 시간 0 으로 넣기
#         visited[case[i][0]][case[i][1]] = 0 # 바이러스가 있던 곳은 0 처리
#     while q:
#         dist,x,y = heapq.heappop(q)
#         if visited[x][y] < dist : continue # 갱신되어 있는데 지금의 거리보다 작으면 넘어가기
#         for i in range(4):
#             nx,ny = x+dx[i],y+dy[i]
#             if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 0 and dist+1<visited[nx][ny]: # 아직 갱신하지 않았거나 기존 시간보다 작다면
#                 visited[nx][ny] = dist+1
#                 heapq.heappush(q,(dist+1,nx,ny))
#         # print(x,y)
#         # for i in range(N):
#         #     print(*visited[i])
#     max_time = 0
#     zero_check = False # 바이러스 확산 후 빈칸이 남아 있는지 체크
#     for i in range(N):
#         for j in range(N):
#             if visited[i][j] == int(1e9) and arr[i][j] == 0 : # 기존에도 빈칸인데 visited도 갱신되지 않았다면 바이러스가 도달하지 못한것 -> 케이스에서 제외해야지
#                 zero_check = True 
#                 break
#             if visited[i][j] != int(1e9) and visited[i][j] > max_time: max_time = visited[i][j]
#         if zero_check : break
#     if not zero_check: answer = min(answer,max_time)