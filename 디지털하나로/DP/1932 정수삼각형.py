import sys
input = sys.stdin.readline

n  = int(input())
arr = [[]]
for _ in range(n):
    arr.append([0]+list(map(int,input().split())))

sum = 0
for i in range(1,n+1):
    sum+=i

dp = [0]*(sum+1)
dp[1] = arr[1][1]
idx = 2

for i in range(2,n+1):
    for j in range(1,i+1):
        if j == 0:
            dp[idx] = dp[idx-i+1] + arr[i][j] 
        elif i == j:
            dp[idx] = dp[idx-i] + arr[i][j]
        else:
            dp[idx] = max( dp[idx-i] + arr[i][j] , dp[idx-i+1] + arr[i][j] )
        idx+=1

print(max(dp))