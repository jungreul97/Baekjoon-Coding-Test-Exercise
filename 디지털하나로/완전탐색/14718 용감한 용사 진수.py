import sys
input = sys.stdin.readline

n,m = map(int,input().split())
warriors = []
answer = int(1e9)
for _ in range(n):
    warriors.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        for k in range(n):
            cnt = 0
            a = warriors[i][0]
            b = warriors[j][1]
            c = warriors[k][2]

            for l in range(n):
                if warriors[l][0]<=a and warriors[l][1]<=b and warriors[l][2]<=c:
                    cnt+=1
            if cnt>=m:
                answer = min(answer,a+b+c)

print(answer)
