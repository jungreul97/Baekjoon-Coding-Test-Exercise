arr = [True] * 10001
for i in range(10001):
    index = i
    s = str(i)
    for j in range(len(s)):
        index+=int(s[j])
    if index>10000:
        continue
    else:
        arr[index] = False
for i in range(1,10001):
    if arr[i]:
        print(i)