# 다이나믹 프로그래밍 ( 동적 계획법 )

# 다이나믹 프로그래밍 조건
# 1. 최적 부분 구조 : 큰 문제를 작은 문제로 나눌 수 있다.
# 2. 중복되는 부분 문제 : 동일한 작은 문제를 반복적으로 해결합니다.

# Ex) 피보나치 수열
# 코드
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)
print(fibo(4))

# 위와 같이 재귀로 풀이를 할 때 fibo(2) 같은 경우 2번이나 실행된다
#       fibo(4)
#        /    \
#  fibo(3)  fibo(2)
#   /     \       \
#fibo(2) fibo(1)  fibo(1)

# 메모리제이션 기법
# 한번 계산한 결과를 메모리 공간메 메모하는 기법
# 위의 피보나치 수열에 대입해 볼 때, 이미 계산된 함수를 생략할 수 있는 장점

# 탑다운 방식
# 예제)
d = [0] * 100
def fibo_topdown(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0: # 이미 계산한 적 있다면 리턴
        return d[x]
    d[x]  = fibo(x-1) + fibo(x-2)
    return d[x]
print(fibo(4))

# 바텀업 방식
# 예제)
d = [0] * 100
d[1] = 1
d[2] = 1
n = 4
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])