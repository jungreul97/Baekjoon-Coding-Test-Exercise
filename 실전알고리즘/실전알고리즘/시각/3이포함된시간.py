#.완전탐색(브루트포스)란 가능한 모든 경우의수를 모두 탐색하여 가짓수를 세는 문제
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1

print(count)