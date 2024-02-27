import sys
input = sys.stdin.readline

a,b = map(int,input().split())
min_n = 0
max_n = 0

max_num = max(a,b)
min_num = min(a,b)

for i in range(min_num,0,-1):
    if a%i == 0 and b%i == 0:
        max_n= i
        break
for i in range(max_num,int(1e9)):
    if i%a == 0 and i%b == 0:
        min_n = i
        break

print(max_n)
print(min_n)