n = int(input())
fac = 1
for i in range(2,n+1):
    fac*=i
str_fac = str(fac)
answer = 0
for i in range(-1,-n,-1):
    if str_fac[i] != '0':
        break
    else:
        answer+=1
if answer == len(str_fac):
    print(0)
else:
    print(answer)
