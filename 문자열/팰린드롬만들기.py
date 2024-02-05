import sys
from collections import Counter
input = sys.stdin.readline

arr = list(map(str, sys.stdin.readline().strip()))
arr.sort()
check = Counter(arr)

cnt = 0
center = ""

for i in check:
    if check[i]%2  != 0 :
        cnt+=1
        center+=i
        arr.remove(i)

    if cnt>1:
        break

if cnt>1:
    print("I'm Sorry Hansoo")
else:
    res=""
    for i in range(0,len(arr),2):
        res+=arr[i]

    print(res+center+res[::-1])




