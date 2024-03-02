# 위상정렬 : 수강과목같이 선후관계가정해진 원소들을 순서대로 나열하는것
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
answer = []
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b) # 앞에 있어야할 학생 뒤에 있어야 할 사람 추가하기
    indegree[b]+=1 # 뒤에 있어야할 학생의 진입 차수 하나 늘리기

queue = deque()

for i in range(1,n+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    x = queue.popleft()
    answer.append(x)

    for i in graph[x]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)
print(*answer,sep= " ")