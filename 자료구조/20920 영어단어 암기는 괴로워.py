import sys
input = sys.stdin.readline

n,standard = map(int,input().split())

dict = {}
for _ in range(n):
    word = input().strip()
    if len(word)<standard:
        continue
    if dict.get(word):
        dict[word][0]+=1
    else:
        dict[word] = [1,len(word),word]

result = sorted(dict.items(), key = lambda x: (-x[1][0], -x[1][1], x[1][2]))

for i in result:
    print(i[0])