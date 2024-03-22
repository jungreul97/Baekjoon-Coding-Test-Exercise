import sys
input = sys.stdin.readline

N = int(input())
gidungs = []
answer = 0
max_gidung = 0
max_gidungs = []
for i in range(N):
    L,H = map(int,input().split())
    gidungs.append((L,H))

gidungs.sort()
max_gidung = 0
max_gidungs = []
for i in range(N):
    H = gidungs[i][1]
    if max_gidung < H : 
        max_gidung = H
        max_gidungs = [] # 초기화 하고 다시 넣기
        max_gidungs.append((i,gidungs[i][0]))
    elif max_gidung == H:
        max_gidungs.append((i,gidungs[i][0])) # 젤높은 기둥의 높이와 같다면 같이 넣기
# 가장 높은 기둥이 있는 왼쪽끝과 오른쪽 끝을 구한다
left_max_idx = max_gidungs[0][1]
right_max_idx = max_gidungs[-1][1]
# 가장높은 기둥들로 둘러쌓인 면적을 구하고
answer += max_gidung * (right_max_idx - left_max_idx + 1)

#왼쪽부터 왼쪽의 가장높은 기둥까지 면적 구하기
max_h = gidungs[0][1]
left_idx = gidungs[0][0]
for i in range(1,max_gidungs[0][0]+1):
    if gidungs[i][1] > max_h:
        answer += (gidungs[i][0]-left_idx) * max_h
        max_h = gidungs[i][1]
        left_idx = gidungs[i][0]

#오른쪽부터 오른쪽의 가장 높은 기둥까지 면적 구하기
max_h = gidungs[N-1][1]
right_idx = gidungs[N-1][0]
for i in range(N-2,max_gidungs[-1][0]-1,-1):
    if gidungs[i][1] > max_h:
        answer += (right_idx - gidungs[i][0]) * max_h
        max_h = gidungs[i][1]
        right_idx = gidungs[i][0]

print(answer)
    