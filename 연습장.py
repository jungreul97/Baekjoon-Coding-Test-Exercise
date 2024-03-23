def cantor(n):
    if n == 1:
        return "-"
    else:
        left = cantor(n//3)
        center = " " * (n //3)
        return left + center + left

while True:
    try:
        N = int(input())
        result = cantor(3**N)
        print(result)
    except:
        break