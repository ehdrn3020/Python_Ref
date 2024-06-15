# 리스트와 튜플은 순서가 있다(인덱싱 가능) / 디셔너리와 섯은 순서가 없다


# map
data = list(map(int, input().split()))


# 순열 - 순서가 다르면 다른 경우의 수
from itertools import permutations
for i in permutations([1,2,3], 2):
	print(i, end=" ")
# 결과 : (1, 2) (1, 3) (2, 1) (2, 3) (3, 1) (3, 2)

# 조합 - 중복 허용하지 않음
from itertools import combinations
for i in combinations([1,2,3], 2):
	print(i, end=" ")
# 결과 : (1, 2) (1, 3) (2, 3)


# 람다 함수 [1]
print((lambda a,b : a+b)(10,5)) # 결과 15

# 람다 함수 [2]
array = [('매트', 50),('로리', 20),('소드', 75)]
def my_key(x):
	return x[1]

sorted(array, key=my_key)
sorted(array, key=lambda x: x[1])