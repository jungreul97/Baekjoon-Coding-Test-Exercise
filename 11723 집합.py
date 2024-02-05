import sys
input = sys.stdin.readline

n = int(input())
s = set()
for _ in range(n):
    command = input().strip().split()
    if len(command) == 1:

        if command[0] == "all":
            s = set([i for i in range(1,21)])
        elif command[0] == "empty":
            s = set()
    else:
        cmd,number = command[0],command[1]
        if cmd == "add":
            s.add(int(number))
        elif cmd == "remove":
            s.discard(int(number))
        elif cmd == "check":
            if int(number) in s:
                print(1)
            else:
                print(0)
        elif cmd == "toggle":
            if int(number) in s:
                s.discard(int(number))
            else:
                s.add(int(number))
    