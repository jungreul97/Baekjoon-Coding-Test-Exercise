import sys
input = sys.stdin.readline

t = int(input())
arr = []
for _ in range(t):
    arr.append(list(map(int,input().split())))

for n in range(t):
    total = 0
    for i in range(1,21):
        for j in range(i+1,21):
            if arr[n][i]>arr[n][j]:
                arr[n][i],arr[n][j] = arr[n][j],arr[n][i]
                total+=1
    print(arr[n][0],total)