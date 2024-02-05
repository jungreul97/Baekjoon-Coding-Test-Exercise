import sys
input  = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(input().rstrip())

hx,hy = 0,0

for i in range(1,n-1):
    for j in range(1,n-1):
        check = True
        if graph[i][j] == graph[i-1][j] == graph[i+1][j] == graph[i][j-1] == graph[i][j+1] == "*":
            hx = i
            hy = j
print(hx+1,hy+1)

result = []
lh = hy
while lh>=0 and graph[hx][lh] == '*':
    lh-=1
result.append(hy-lh-1)
rh = hy
while rh<n and graph[hx][rh] == '*':
    rh+=1
result.append(rh-hy-1)
hurry = hx
while hurry<n and graph[hurry][hy] == '*':
    hurry+=1
result.append(hurry-hx-1)

llx,lly = hurry,hy-1
while llx<n and graph[llx][lly] == "*":
    llx+=1
result.append(llx-hurry)
rlx,rly = hurry,hy+1
while rlx<n and graph[rlx][rly] == "*":
    rlx+=1
result.append(rlx-hurry)

for i in result:
    print(i,end=' ')



