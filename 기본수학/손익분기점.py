a,b,c = map(int,input().split())
total = 0
sell = 0
n = 0

if b>=c:
    print(-1)
else:
    print(a//(c-b)+1)
