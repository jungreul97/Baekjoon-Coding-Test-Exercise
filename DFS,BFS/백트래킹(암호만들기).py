import sys
input = sys.stdin.readline

def back_tracking(cnt,idx):
    if cnt == n:
        mo,ja = 0,0
        for i in range(n):
            if answer[i] in consonant:
                mo+=1
            else:
                ja+=1
        
        if mo>=1 and ja>=2:
            print("".join(answer))
        
        return
    for i in range(idx,m):
        answer.append(arr[i])
        back_tracking(cnt+1,i+1)
        answer.pop()


n,m = map(int,input().rstrip().split())

arr = sorted(list(map(str,input().rstrip().split())))
consonant = ['a','e','i','o','u']
answer = []

back_tracking(0,0)
