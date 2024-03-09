import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = list(map(int,input().split()))
sum_arr = [0]*(N+1)
sum_arr[1] = arr[0]
for i in range(2,N+1):
    sum_arr[i] = sum_arr[i-1]+arr[i-1]

for _ in range(M):
    i,j = map(int,input().split())
    print(sum_arr[j] - sum_arr[i-1])