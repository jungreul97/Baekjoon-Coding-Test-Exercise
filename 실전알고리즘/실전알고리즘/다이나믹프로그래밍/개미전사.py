# from array import array


# n = int(input())
# array = list(map(int,input().split()))

# d = [0]*100

# d[0] = array[0]
# d[1] = max(array[0],array[1])
# for i in range(2,n):
#     d[i] = max(d[i-1],d[i-2]+array[i])

# print(d[n-1])

n = int(input())
arr = list(map(int,input().split()))

d = [0]*100
d[0] = arr[0]
d[1] = max(arr[0],arr[1])
for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+arr[i])
for i in range(n):
    print(d[i],end = " ")
print(d[n-1])

