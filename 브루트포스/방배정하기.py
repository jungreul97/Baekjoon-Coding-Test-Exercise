a,b,c,n = map(int,(input().split()))

result = n
for i in range(n//a):
    for j in range(n//b):
        for k in range(n//c):
            if (a*i)+(b*j)+(c*k) == n:
                if i+j+k<result:
                    result = i+j+k

if result == n :
    print(0)
else:
    print(1)