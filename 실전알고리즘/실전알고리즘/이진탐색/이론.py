# 이진탐색 : 정렬되어 있는 리스트에서 탐색범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
# 시작점, 끝점, 중간점을 이용해서 탐색범위를 정함 log2,N의 시간복잡도를 가짐

def binary_search(array,target,start,end):
    if start>end:
        return None
    mid = (start+end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return  binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

def binary_search1(array,target,start,end):
    while start<=end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid+1
    return None

arr = [0,2,3,4,8,10,12,14,16,18]
n = len(arr)
result = binary_search1(arr,4,0,n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)

# 파이썬 이진탐색 라이브러리
# bisect_left : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환함
# bisect_right : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환함
from bisect import bisect_left,bisect_right
a = [1,2,4,4,8]
x = 4
print(bisect_left(a,x))
print(bisect_right(a,x))

# bisect를 이용해서 특정 범위에 속하는 데이터 갯수 구하기 
def count_by_range(a,left_value,right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a,4,4))
print(count_by_range(a,-1,3))

# 파라메트릭 서치 : 

