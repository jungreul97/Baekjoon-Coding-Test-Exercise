import heapq

def heapsort(iterable):
    h = []
    result=[]
    for value in iterable:
        #힙에 넣을때 데이터의 부호를 바꿔서 넣으면 내림차순으로 정렬 가능
        heapq.heappush(h,-value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)