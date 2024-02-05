#선택정렬 : 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복함(O(N^2))
array = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[j]<array[min_index]:
            min_index = j
    array[i],array[min_index] = array[min_index],array[i]
print(array)

#삽입정렬 : 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입함, 선택정렬에 비해 효율적임
array = [7,5,9,0,3,1,6,2,4,8]
for i in range(1,len(array)): # 정렬되지 않은 오른쪽의 첫 원소를 정렬된 배열을 탐색을 하며 한자리씩 순서대로 스왑하면서 내려감
    for j in range(i,0,-1):
        if array[j]<array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
        else:
            break #이미 정렬된 배열에서 가장 큰 숫자보다 크니까 더 탐색할 필요가 없음
print(array)
#삽입정렬의 시간복잡도는 O(N^2)이며 가장 최선의 경우 O(N)의 시간복잡도를 가질수 있음

#퀵정렬 : 기준 데이터를 설정하고 기준 데이터보다 작은 데이터의 위치를 바꾸는 방법, 일반적인 상황에서 가장 많이 사용되는 알고리즘
# 평균의 경우 O(NlogN)의 시간 복잡도를 가짐, 최악의 경우 (O(N^2))의 복잡도가 발새할 수 있음
array = [7,5,9,0,3,1,6,2,4,8]
def quick_sort(array,start,end):
    if start>=end:
        return
    pivot = start
    left = pivot+1
    right = end
    while left<=end and array[left]<=array[pivot]:
        left+=1
    while right>start and array[right]>=array[pivot]:
        right-=1
    if left>right:
        array[pivot],array[right] = array[right],array[pivot]
    else:
        array[left],array[right] = array[right],array[left]
    
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)
    
# 계수정렬 : 특정 조건이 부합할때만 사용할 수 있음 매우 빠르게 동작함, 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용가능함
# 데이터의 개수가 n개, 데이터(양수) 중 최댓값이 k일 때 최악의 경우에도 수행시간 (O + K)를 보장함
# ㅋㅋ 구냥 원소자체를 배열의 인덱스로 넣어 해당 양수가 몇번 출현했는지 계산해서 쭉 나열하는 거네
array = [7,5,9,0,3,1,6,2,4,8,0,5,2]
count = [0] * (max(array)+1)
for i in range(len(array)):
    count[array[i]]+=1
for i in range(len(count)):
    for j in range(count[i]):
        print(i,end = ' ')