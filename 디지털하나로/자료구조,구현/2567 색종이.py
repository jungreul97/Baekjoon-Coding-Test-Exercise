import sys
input = sys.stdin.readline

n = int(input())
edge = []
for i in range(n):
    a,b = map(int,input().split())
    edge.append((a,b))
graph = [[0]*101 for i in range(101)]

for i,j in edge:
    for k in range(i,i+10):
        for l in range(j,j+10):
            graph[k][l] = 1
total = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(1,101):
    for j in range(1,101):
        if graph[i][j] == 1:
            tmp = 0
            for k in range(4):
                if graph[i+dx[k]][j+dy[k]] == 1:
                    tmp+=1
            if tmp == 3:
                total+=1
            elif tmp == 2:
                total+=2
print(total)





