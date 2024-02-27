import sys
input = sys.stdin.readline
arr = []
max_num = 0
x,y = 0,0
for _ in range(9):
    arr.append(list(map(int,input().split())))

for i in range(9):
    for j in range(9):
        if arr[i][j] > max_num :
            max_num = arr[i][j]
            x,y = i,j

print(max_num)
print(x+1,y+1)