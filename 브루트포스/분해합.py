n = int(input())

result = 0

for i in range(1,n+1):
    arr = list(map(int,str(i)))
    if i+sum(arr) == n:
        result = i
        break

if result == n:
    print(0)
else:
    print(result)
    

