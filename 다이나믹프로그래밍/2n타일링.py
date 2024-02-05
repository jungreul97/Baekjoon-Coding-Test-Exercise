n = int(input())

result = [0 for i in range(1001)]
result[1] = 1
result[2] = 2
result[3] = 3
result[4] = 5
for i in range(5,1001):
    result[i]  = result[i-2]+result[i-1]

print(result[n]%10007)