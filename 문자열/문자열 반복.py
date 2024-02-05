n = int(input())
re = []
s = []
for i in range(n):
    a,b = input().split()
    re.append(int(a))
    s.append(b)

for i in range(n):
    for j in s[i]:
        print(re[i]*j,end="")
    print()

    


