n,k = map(int,input().split())

coin = []
result = 0
for i in range(n):
    coin.append(int(input()))

index = n
while True:
    index-=1
    if k//coin[index] == 0:
        continue
    else:
        result+=k//coin[index]
        if k%coin[index]==0:
            break
        else:
            k = k%coin[index]

print(result)