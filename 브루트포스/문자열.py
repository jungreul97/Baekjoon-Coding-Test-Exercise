import sys
input = sys.stdin.readline

x,y = input().rstrip().split()

result = 0
if len(x) == len(y):
    for i in range(len(x)):
        if x[i] != y[i]:
            result+=1
    print(result)
elif x in y:
    print(0)
else:
    result = []
    maxn = len(x)-1
    check = True
    while check:
        for i in range(len(x)-maxn+1):
            # print(x[i:i+maxn])
            if x[i:i+maxn] in y:
                check = False
                break
        if not check : break
        maxn-=1
    result.append(len(x)-maxn)
    result1 = 0
    result2 = 0
    for i in range(len(x)):
        if x[i]!= y[i]:
            result1+=1
    yarr = y[len(y)-len(x):]
    for i in range(len(x)-1,-1,-1):
        if yarr[i] != x[i]:
            result2+=1
    result.append(result1)
    result.append(result2)
    print(min(result))





