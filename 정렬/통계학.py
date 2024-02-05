from collections import Counter


n = int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))

arr.sort()
print(round(sum(arr)/n))
print(arr[len(arr)//2])

cnt = Counter(arr).most_common()
if len(arr)>1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(max(arr)-min(arr))