n = int(input())
arr = list(map(int,input().split()))

result = 0
for i in arr:
    if i == 2 or i == 3:
        result+=1
    elif i == 1 or i%2 == 0 or i%3 == 0:
        continue
    else:
        check = True
        for j in range(5,i):
            if i%j == 0:
                check = False
        if check:
            result+=1

print(result)

        

