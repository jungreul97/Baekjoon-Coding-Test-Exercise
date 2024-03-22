import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
words = list(map(str,input().rstrip().split()))
dict = defaultdict(int)
for word in words:
    if word[-6:] == "Cheese":
        dict[word]+=1
if len(dict)>=4: print("yummy")
else: print("sad")

