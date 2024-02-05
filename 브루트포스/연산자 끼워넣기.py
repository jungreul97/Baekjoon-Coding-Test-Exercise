from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().strip().split()))
command = list(map(int,input().strip().split()))

san = ['+','-','*','/']

cmd = []
index = -1
for i in command:
    index+=1
    for _ in range(i):
        cmd.append(san[index])

cases = permutations(cmd)
for case in cases:
    print(case)