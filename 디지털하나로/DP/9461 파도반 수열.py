import sys
input = sys.stdin.readline

dp = [0]*101
dp[1],dp[2],dp[3],dp[4],dp[5] = 1,1,1,2,2
start = 1
for i in range(6,101):
    dp[i] = dp[start] + dp[i-1]
    start+=1
print(dp)


T = int(input())
while T>0:
    N = int(input())
    print(dp[N])
    T-=1