n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

result = []

for i in arr:
    maxt = 0
    for j in range(1,i):
        if j+(j*j)>i:
            break
        else:
            maxt = j
    result.append(maxt)

for i in result:
    print(i)