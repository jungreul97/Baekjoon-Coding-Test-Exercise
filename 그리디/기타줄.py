import sys
input = sys.stdin.readline

n,b = map(int,input().split())

list_a = []
list_b = []
result = 0
result_b = 0

for _ in range(b):
    x,y = map(int,input().split())
    list_a.append(x)
    list_b.append(y)

list_a.sort()
list_b.sort()

# print(list_a)
# print(list_b)
if b == 1:
    print(min(list_a[0]*((n//6)+1),list_b[0]*n))
else:
    x = n//6
    y = int(n%6)
    print(min(list_a[0]*(x+1),(list_a[0]*x)+list_b[0]*y,(list_b[0]*n)))