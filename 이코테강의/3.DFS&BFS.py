### 그래프 탐색 알고리즘 DFS/BFS
# 탐색 알고리즘으로 많이 등장하는 유형


# [ 스택 구현 예제 ]
stack = []
stack.append(5)
stack.append(4)
stack.pop()
stack.append(3)
stack.append(2)
stack.pop()
print(stack)
# >>> [5, 3]
print(stack[::-1]) # 스택 역순
# >>> [3, 5]


# [ 큐 구현 예제 ]
from collections import deque
queue = deque()
queue.append(5)
queue.append(4)
queue.append(3)
queue.popleft()
queue.append(2)
queue.append(1)
queue.popleft()
print(queue)
# >>> deque([3, 2, 1])
queue.reverse() # 역순으로 변경
print(queue)
# >>> deque([1, 2, 3])


# [ 재귀 함수 ( Recursive Function ) ]
# 종료조건이 필요
# 예제 )
def recursive_function(i):
    if i == 4:
        return
    print(f'{i}st function call')
    recursive_function(i+1)
    print(f'{i}st function end')
recursive_function(1)
# >>> 출력 결과
# 1st function call
# 2st function call
# 3st function call
# 3st function end
# 2st function end
# 1st function end

# 문제 1) 팩토리얼 구현 ( n! = 1 * 2 * 3 * .. n )
def factorial_func(n):
    if n <= 1:
        return 1
    return n * factorial_func(n - 1)


# [ DFS ( Depth-First Search ) ]
# 깊이 우선 탐색이라고 부르며, 스택 혹은 재귀함수를 이용한다.
# 예제 )
# 노드 정보를 2차원 배열로 표현
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 방문된 정보
visited = [False] * 9
dfs(graph, 1, visited)


# [ BFS ( Breadth-First Search ) ]
# 너비 우선 탐색이라고 하며, 큐 자료구조를 이용하여 구현한다.
# 예제 )
from collections import deque
def bfs(grach, start, visiterd):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * 9
bfs(grach, 1, visiterd)



# [ BFS / DFS 문제 ]

# 문제 ) 음료수 얼려먹기 - DFS
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력


# 문제 ) 미로 탈출 (인접한 최단거리 ) - BFS
from collections import deque

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append(x, y)
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 미로 찾기 공간을 벗어난 경우 무시
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                # 벽인 경우 무시
                if graph[nx][ny] == 0:
                    continue
                # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
                # 가장 오른쪽 아래까지의 최단 거리 반환
            return graph[n - 1][m - 1]

print(bfs(0, 0))