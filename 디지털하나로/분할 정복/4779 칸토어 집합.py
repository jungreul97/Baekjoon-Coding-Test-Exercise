import sys
input = sys.stdin.readline

def merge_sort(s):
    n = len(s)
    if len(s) == 1: 
        return s
    else:
        left = merge_sort(s[:n//3])
        mid = " "*(n//3)
        return left + mid + left

while True:
    try:
        N = int(input())
        print(merge_sort("-"*(3**N)))
    except:
        break
