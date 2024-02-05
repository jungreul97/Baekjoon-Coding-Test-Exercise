n = int(input())
health = list(map(int,input().split()))
happy = list(map(int,input().split()))

health,happy = [0]+health, [0]+happy


dp = [[0 for i in range(101)]for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,101):
        if health[i]<=j:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-health[i]]+happy[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])
