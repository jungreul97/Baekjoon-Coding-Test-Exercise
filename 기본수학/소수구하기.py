m,n = map(int,input().split())

for i in range(m,n+1):
    check = True
    cnt = 0
    if i == 1:
        continue
    else:
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                check = False
                break
    if check:
        print(i)
