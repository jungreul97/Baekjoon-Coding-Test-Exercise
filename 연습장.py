import sys
input = sys.stdin.readline

T = int(input())
while T>0:
    N = int(input())
    print(sum(list(map(int,input().split()))))
    T-=1