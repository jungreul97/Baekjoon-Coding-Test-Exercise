n = int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

result = [1 for i in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            result[i]+=1
        else:
            continue

for i in result:
    print(i,sep=" ")