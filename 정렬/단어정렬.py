n = int(input())
arr=[]
for _ in range(n):
    arr.append(input())

arr = list(set(arr))#set은 중복된거 안받음 넣을때 add로 넣기

arr.sort()
arr.sort(key = len)

for i in arr:
    print(i)
