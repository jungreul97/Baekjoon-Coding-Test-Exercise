import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

sum_arr = [[0]*N for _ in range(N)]
total = 0
for i in range(N):
    for j in range(N):
        total+=arr[i][j]
        sum_arr[i][j] = total
# for i in range(N):
#     print(arr[i])
# for i in range(N):
#     print(sum_arr[i])


for _ in range(M):
    a,b,c,d = map(int,input().split())
    #입력한 수에서 1씩 빼주어 배열 인덱스 맞추기
    a-=1
    b-=1
    c-=1
    d-=1

    total = 0 # 정답
    if a==c and b == d: total = arr[a][b] # 한칸이라면 그냥 배열에서 출력
    elif b == 0 : # 배열중 시작 컬럼이 0 이라면 
        for i in range(a,c+1):
            if i == 0: total += sum_arr[i][d] # 첫번째 줄이라면 그냥 배열구간합 더해주고
            else: total += sum_arr[i][d] - sum_arr[i-1][N-1] # 2번째줄 부터는 구간합에서 윗줄의 마지막칸합까지를 빼준 것을 total에 더함
    else: # 그냥 가운데의 범위를 알고 싶다면
        b-=1 
        for i in range(a,c+1):
            total += sum_arr[i][d] - sum_arr[i][b] #해당줄의 마지막원소의 구간합에서 첫컬럼보다 -1 컬럼의 구간합을 빼준값을 더해줌 매줄마다
    print(total)
