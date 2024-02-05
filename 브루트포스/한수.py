arr = [True] * 1001

for i in range(1,len(arr)):
    s = str(i)
    if len(s) == 1 or len(s) == 2:
        continue
    elif len(s) == 3:
        if int(s[0])-int(s[1]) == int(s[1])-int(s[2]):
            continue
        else:
            arr[i] = False
    else:
        arr[i] = False

n = int(input())
result = 0
for i in range(1,n+1):
    if arr[i]:
        result+=1

print(result)
