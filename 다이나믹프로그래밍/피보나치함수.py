arr0 = [1,0,1]
arr1 = [0,1,1]

def fibo(n):
    if len(arr0)<=n:
        for i in range(len(arr0),n+1):
            arr0.append(arr0[i-1]+arr0[i-2])
            arr1.append(arr1[i-1]+arr1[i-2])
    print(arr0[n],arr1[n])

t = int(input())

for _ in range(t):
    fibo(int(input()))