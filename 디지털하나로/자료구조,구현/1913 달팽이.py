import sys
input = sys.stdin.readline

n = int(input())
target = int(input())
answer_x,asnwer_y = 0,0
state = 'up'
start_n = 0
arr = [[0]*n for _ in range(n)]
x,y = n//2,n//2
end_n = 1

for number in range(1,n**2+1):
    arr[x][y] = number
    if number == end_n**2:
        x-=1
        end_n+=2
        state = 'right'
        start_n = number+1
    elif state == 'up': 
        x-=1
    elif state == 'right':
        if number == start_n+end_n-2:
            state = 'down'
            start_n = number
            x+=1
        else:
            y+=1
    elif state == 'down':
        if number == start_n+end_n-1:
            state = 'left'
            start_n = number
            y-=1
        else:
            x+=1
    elif state == 'left':
        if number == start_n+end_n-1:
            state = 'up'
            start_n = number
            x-=1
        else:
            y-=1

    if number+1 == n ** 2:
        arr[x][y] = number+1
        break    
for i in range(n):
    for j in range(n):
        if arr[i][j] == target : answer_x,answer_y = i,j
        print(arr[i][j],end=' ')
    print()
print(answer_x+1,answer_y+1)

