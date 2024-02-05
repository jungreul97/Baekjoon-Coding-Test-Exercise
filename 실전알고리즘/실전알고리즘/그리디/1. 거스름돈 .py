n = 1260
arr = [500,100,50,10]
result = 0

for i in range(len(arr)):
    result+= n // arr[i]
    n %= arr[i]

print(result)