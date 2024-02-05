a,b = list(map(int,input().split()))
c = a
d = b
if d<45:
    d = 60+(d-45)
    if c == 0:
        c = 23
    else:
        c = c-1
else:
    d = d-45

print(c,d)