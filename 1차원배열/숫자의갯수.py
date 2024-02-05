a = int(input())
b = int(input())
c = int(input())

mulnum = a*b*c
strnum = str(mulnum)
numlist = [0 for i in range(10)]

for i in range(len(strnum)):
    numlist[int(strnum[i])]+=1

for i in range(10):
    print(numlist[i])
