import sys
m = int(input())
n = int(input())

arr = []
min = sys.maxsize

for i in range(m,n+1):
    check = 0
    if i == 1:
        continue
    for j in range(2,i+1):
        if i%j == 0:
            check +=1
            if check>=2:
                break
    if check == 1:
        arr.append(i)
        if i<min:
            min = i

if len(arr)==0:
    print(-1)
else:
    print(sum(arr))
    print(min)