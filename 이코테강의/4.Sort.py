# [ 선택 정렬 ]
# 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복
# 0 5 9 7 3
# 0 3 5 9 7
# 0 3 5 7 9

# 예제 - 이중 반복문
# 시간복잡도 : O(N제곱)
array = [7,5,9,0,3,1,2]
for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]
print(array)


# [ 삽입 정렬 ]
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
# 선택 정렬에 비해 구현난이도가 높지만, 더 효율적으로 동작

# 예제 - 이중 반복문, 두번째 반복문은 역순으로 반복
# 시간복잡도 : 최소 O(N) ~ 최대 O(N제곱)
array = [7,5,9,0,3,1,2]
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
print(array)


# [ 퀵 정렬 ]
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 기본적인 퀵 정렬은 첫번째 데이터를 기준 데이터(Pivot)로 설정
# 퀵정렬은 재귀적으로 수행되고 정렬이 수행될 때마다 대상요소가 적어진다.

# 시간복잡도 : 평균 O(N log N) ~ 최대 O(N제곱)
array = [7,5,9,0,3,1,2]
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
