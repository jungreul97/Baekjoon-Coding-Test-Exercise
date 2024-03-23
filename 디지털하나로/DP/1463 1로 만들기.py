import sys
input= sys.stdin.readline

N = int(input())
dp = [int(1e9)]*(N+1)
dp[N] = 0

idx = N
while True:
    if idx == 1: break
    if idx%3 == 0 and dp[idx//3] > dp[idx]+1:
        dp[(idx//3)] = dp[idx]+1
    if idx%2 == 0 and dp[idx//2] > dp[idx]+1:
        dp[(idx//2)] = dp[idx]+1
    if dp[idx-1] > dp[idx]+1:
        dp[idx-1] = dp[idx]+1
    idx-=1
    
print(dp[1])

