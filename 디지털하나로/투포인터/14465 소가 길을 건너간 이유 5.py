import sys
input = sys.stdin.readline

N,K,B = map(int,input().split())
arr = [0] * (N+1)
for _ in range(B):
    arr[int(input())] = 1
# print(arr)

min_num = sum(arr[1:K+1])
cnt = min_num
#cnt는 해당 윈도우 안의 부서진 신호등 갯수 윈도우를 오른쪽으로 옮겨가며 부서진 신호등 갯수 줄이고 더하기 
for i in range(2,N-K+2):
    if arr[i-1] == 1:
        cnt-=1 
    if arr[i+K-1] == 1:
        cnt+=1
    # print(i,cnt)
    min_num = min(cnt,min_num)
    if min_num == 0:
        break

print(min_num)
