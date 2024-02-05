n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key = lambda x:x[0]) #시작시간 먼저 정렬후
arr.sort(key = lambda x:x[1]) #끝나는 시간 빠른 순서대로 정렬

cnt = 1
end = arr[0][1]
for i in range(1,n):
    if arr[i][0]>=end:
        cnt+=1
        end = arr[i][1]

print(cnt)