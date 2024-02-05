n = int(input())
data = input().split()
move_types = ['R','U','L','D']
dx = [0,-1,0,1]#동북서남 방향으로 방향벡터, 행의 움직임
dy = [1,0,-1,0]#열의 움직임 방향 벡터
x=1
y=1

for d in data:
    for i in range(len(move_types)):
        if d == move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    if nx<1 or ny<1 or nx>n or ny>n: #배열을 벗어나면 미반영
        continue

    x,y = nx,ny # 배열을 벗어나지 않는다면 반영

print(x,y)        
    
