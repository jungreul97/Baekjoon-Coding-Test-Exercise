from collections import Counter
arr = list(input())

numlist = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}
for i in arr:
    if i in ['6','9']:
        numlist['6']+=1
    else:
        numlist[i]+=1

if numlist['6']%2 == 0:
    numlist['6']//=2
else:
    numlist['6'] = (numlist['6']//2)+1
print(max(numlist.values()))