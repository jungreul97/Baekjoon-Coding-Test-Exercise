from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dict = defaultdict(int)
students = list(map(int,input().rstrip().split()))
photo = []
for i in range(m):
    dict[i]+=1
    if i in photo:
        continue
    elif len(photo)<n:
        photo.append(i)
    elif len(photo) == n:
        min_v = 10000
        for k in photo:
            if dict[k]<min_v:
                min_v = dict[k]
                d = k
        else:
            photo.remove(d)
            del(dict[d])
            photo.append(i)

photo = list(map(int,photo))
photo.sort()
print(*photo)
