numlist=[]
for i in range(10):
    numlist.append(int(input()))
lastlist = [0 for i in range(42)]

for i in range(10):
    p = numlist[i]%42
    if lastlist[p] == 0:
        lastlist[p] += 1
    else:
        continue

result = 0
for i in lastlist:
    if i == 1:
        result+=1

print(result)

