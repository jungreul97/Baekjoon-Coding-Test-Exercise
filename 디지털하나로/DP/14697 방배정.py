import sys
input = sys.stdin.readline

a,b,c,n = map(int,input().split())

arr = [a,b,c]
dp = [0]*(n+1)
dp[0] = 1
for i in range(1,n+1):
    for num in arr:
        if i-num >=0 and dp[i-num]:
            dp[i] = 1
print(dp[n])