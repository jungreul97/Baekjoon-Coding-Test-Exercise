n = int(input())

row = 0
order = 0

while order+row+1<n:
    row+=1
    order+=row

if row % 2 == 0 :
    col=1
    row+=1
    for i in range(n-order-1):
        col+=1
        row-=1
else:
    col = row+1
    row = 1
    for i in range(n-order-1):
        row+=1
        col-=1

print(row,col,sep="/")
