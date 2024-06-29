# 그리디 & 구현 알고리즘

### 그리디 알고리즘(탐욕법)은 현재 상황에서 최적의 해를 항상 보장하는 방법을 적용

# 문제1 ) 거스름돈 문제 - 손님에게 거슬러 줘야 할 돈이 N 일 때 거슬러 주어야할 동전(500,100,10)의 최소 개수 구하기
# 풀이 ) 가장 큰 화페 단위부터 돈을 거슬러 준다
# 그리디 적용 조건 ) 큰 단위가 항상 작은 단위의 배수 ( 400 동전이 있고 800원을 거슬러 줄 때 배수가 아니다 )
# 코드 )
n = 1260
count = 0
array = [500, 100, 50, 10]
for coin in array:
    count += n // coin
    n %= coin
print(count)
# 시간복잡도 O(K)

# 문제2 ) 각 자리가 숫자로 이루어진 문자열(S), 왼쪽부터 x,+ 숫자 사이에 넣으며 만들어질 수 있는 가장 큰 수 구하기
# 풀이 ) 두 수중에 하나라도 1 이하인 경우 더하며, 두 수가 모두 2이상이면 곱한다.
# 코드 )
data = input()
result = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)



### 구현알고리즘은 범위가 포괄적, 풀이를 떠올리는 것을 쉽지만 소스코드로 옮기기 어려운 문제

# 문제1 ) 상하좌우 문제 ( 구현유형, 완전탐색유형, 시뮬레이션 유형은 비슷함 )
# 입력예시 5 / R R R U D D
# 출력예시 3 4
# 코드 )
n = int(input())
plans = input().split()
x, y  = 1,1
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        nx = x + dx[i]
        ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)