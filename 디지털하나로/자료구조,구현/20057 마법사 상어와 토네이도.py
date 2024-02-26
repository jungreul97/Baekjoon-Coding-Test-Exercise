import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
x,y = n//2,n//2
total = 0
left = [(0,-2,0.05),(-1,-1,0.1),(1,-1,0.1),(-1,0,0.07),(-2,0,0.02),(1,0,0.07),(2,0,0.02),(-1,1,0.01),(1,1,0.01)]
right = [(0,2,0.05),(1,1,0.1),(-1,1,0.1),(-1,0,0.07),(-2,0,0.02),(1,0,0.07),(2,0,0.02),(-1,-1,0.01),(1,-1,0.01)]
up = [(-2,0,0.05),(-1,-1,0.1),(-1,1,0.1),(0,-1,0.07),(0,-2,0.02),(0,1,0.07),(0,2,0.02),(1,1,0.01),(1,-1,0.01)]
down = [(2,0,0.05),(1,-1,0.1),(1,1,0.1),(0,-1,0.07),(0,-2,0.02),(0,1,0.07),(0,2,0.02),(-1,1,0.01),(-1,-1,0.01)]
state = 'left'
dist = 1 # 이동해야 하는 거리
shift = 0 # 해당방향으로 이동한 거리

while x!=0 or y!=0: # x나 y중 하나라도 0이 아니면 실행!!
    shift +=1
    remain = 0
    # print(x,y,state)
    if state == 'left':
        y-=1
        remain = arr[x][y]
        if remain != 0:
            for cmd in left:
                nx,ny = x+cmd[0],y+cmd[1]
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    total+=int(arr[x][y]*cmd[2]) # 격자 밖으로 나간거 total에 +
                else:
                    arr[nx][ny] += int(arr[x][y]*cmd[2]) # 격자안에 것 원래것에서 합치기
                remain-= int(arr[x][y]*cmd[2])
            if y-1>=0:
                arr[x][y-1] += remain
            else: 
                total+=remain
            arr[x][y] = 0        
        if shift == dist: # 만약 해당방향으로 이동해야 하는 거리만큼 갔다면
            state = 'down' # 이동방향 갱신하고
            shift = 0 # 이동해야할 거리 초기화
    elif state =='down':
        x+=1
        remain = arr[x][y]
        if remain != 0:
            for cmd in down:
                nx,ny = x+cmd[0],y+cmd[1]
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    total+=int(arr[x][y]*cmd[2])
                else:
                    arr[nx][ny] += int(arr[x][y]*cmd[2])
                remain -= int(arr[x][y]*cmd[2])
            if x+1<n:
                arr[x+1][y] += remain
            else:
                total+=remain
            arr[x][y] = 0 
        if shift == dist:
            state = 'right' 
            shift = 0 
            dist+=1 # 오른쪽으로는 한칸 더 늘어남   
    elif state == 'right':
        y+=1
        remain = arr[x][y]
        if remain != 0:
            for cmd in right:
                nx,ny = x+cmd[0],y+cmd[1]
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    total+=int(arr[x][y]*cmd[2])
                else:
                    arr[nx][ny] += int(arr[x][y]*cmd[2])
                remain -= int(arr[x][y]*cmd[2])
            if y+1<n:
                arr[x][y+1] +=remain
            else:
                total+=remain        
            arr[x][y] = 0
        if shift == dist:
            state = 'up' 
            shift = 0 
    else:
        x-=1
        remain = arr[x][y]
        if remain != 0:
            for cmd in up:
                nx,ny = x+cmd[0],y+cmd[1]
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    total+=int(arr[x][y]*cmd[2])
                else:
                    arr[nx][ny] += int(arr[x][y]*cmd[2])
                remain -= int(arr[x][y]*cmd[2])
            if x-1>=0:
                arr[x-1][y] += remain
            else:
                total+=remain
            arr[x][y] = 0
        if shift == dist:
            state = 'left' 
            shift = 0
            dist += 1
    # for i in range(n):
    #     print(*arr[i])
    # print("----total-----", total)
print(total)
        



