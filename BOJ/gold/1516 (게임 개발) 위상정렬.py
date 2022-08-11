
'''
문제 예제에서 10 다음에 20이 나오는 이유는,
2번째 건물 짓는데 걸리는 시간이 20이라서. 20이 14보다 빠르다는 의미가 아니다.

'''

# from collections import deque
#
# n = int(input())
#
# times = [0 for _ in range(n + 1)]  # 소요시간
# input_cnt = [0 for _ in range(n + 1)]  # 진입 가능 갯수
# table = dict()  # 어디로 연결되어 있는지.
#
# for i in range(n):
#     arr = [x for x in list(map(int, input().split())) if x != -1]
#     times[i + 1] = arr[0]
#
#     for k in arr[1:]:
#         if k not in table:
#             table[k] = [i + 1]
#         else:
#             table[k].append(i + 1)  # 첫 번째 값을 제외한 나머지 다 넣음
#
#     input_cnt[i + 1] = len(arr[1:])
#
# q = deque()
# for x in range(1, n + 1):
#     if input_cnt[x] == 0:
#         q.append(x)  # 시작점 집어넣기
#         input_cnt[x] = -1  # 넣었다고 표기
#
# result = [0 for _ in range(n + 1)]
#
# while q:
#     node = q.popleft()
#     if node not in table:
#         continue
#     else:
#         for k in table[node]:
#             result[k] = max(times[node], result[node] + times[node])
#             if input_cnt[k] > 0:  # 0이면 그냥 패스
#                 input_cnt[k] -= 1
#     for idx, x in enumerate(input_cnt[1:]):
#         if x == 0:
#             q.append(idx + 1)
#             input_cnt[idx + 1] = -1
#
# for x in range(1, len(times)):
#     print(times[x] + result[x])

# 8%에서 틀림

'''
5
10 -1
20 1 -1
30 2 -1
40 3 5 -1
100 -1
이런 반례가 있다.

답은
10
30
60
140
100
이 나와야 함.
'''

from collections import deque

n = int(input())

times = [0 for _ in range(n + 1)]  # 소요시간
input_cnt = [0 for _ in range(n + 1)]  # 진입 가능 갯수
table = dict()  # 어디로 연결되어 있는지.

for i in range(n):
    arr = [x for x in list(map(int, input().split())) if x != -1]
    times[i + 1] = arr[0]

    for k in arr[1:]:
        if k not in table:
            table[k] = [i + 1]
        else:
            table[k].append(i + 1)  # 첫 번째 값을 제외한 나머지 다 넣음

    input_cnt[i + 1] = len(arr[1:])

print(table)

q = deque()
for x in range(1, n + 1):
    if input_cnt[x] == 0:
        q.append(x)  # 시작점 집어넣기
        input_cnt[x] = -1  # 넣었다고 표기

result = [0 for _ in range(n + 1)]

while q:
    node = q.popleft()
    if node not in table:
        continue
    else:
        for k in table[node]:
            result[k] = max(times[k] + result[k], times[node]) # 이 코드부분, 여기가 문제다.

            if input_cnt[k] > 0:  # 0이면 그냥 패스
                input_cnt[k] -= 1

    for idx, x in enumerate(input_cnt[1:]):
        if x == 0:
            q.append(idx + 1)
            input_cnt[idx + 1] = -1
    print(input_cnt, result, times)

for x in range(1, len(times)):
    print(times[x] + result[x])





## 다른 사람 코드 ##
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())
queue = deque()
indegree = [0] * (N + 1)
arr = [[0] * (N + 1) for _ in range(N + 1)] # 행렬 꼴로 만듦.
time = [0] * (N + 1)

for i in range(1, N + 1):
    _input = list(map(int, input().split()))
    time[i] = _input[0]
    for x in _input[1:-1]: # 맨 처음 값과, 끝 값 제외
        arr[i][x] = 1
        indegree[i] += 1

for i in range(1, N + 1):
    if indegree[i] == 0: # 진입차수 0인 경우를
        queue.append(i) # 큐에 넣는다.

while queue:
    x = queue.popleft()
    t = 0

    for i in range(1, N + 1):
        if arr[i][x] == 1:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
        if arr[x][i] == 1:
            t = max(time[i], t) # 이 부분 코드가 핵심.
    time[x] += t

for i in time[1:]:
    print(i)




    




import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

# 노드와 간선의 정보 저장
building = [[] for _ in range(N + 1)]
# 각 노드의 진입차수
indegree = [0] * (N + 1)
# 건물 짓는데 걸리는 시간
cost = [0] * (N + 1)

for i in range(1, N + 1):
    data = list(map(int, input().split()))[:-1]
    cost[i] = data[0]
    building_data = data[1:]

    # 간선 연결 및 진입차수 설정
    for j in building_data:
        building[j].append(i)
        indegree[i] += 1


# 위상 정렬 함수
def topology_sort():
    result = [0] * (N + 1)
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        # 큐에서 꺼낸 노드 번호에 해당하는 건물을 짓는데 걸리는 시간 저장
        # 선수 건물 짓는데 걸리는 시간이 포함되어 있음!
        # 즉, '선수 건물 짓는데 걸리는 시간 + 현재 건물 짓는데 걸리는 시간'이 저장됨
        result[now] += cost[now]
        for b in building[now]:
            indegree[b] -= 1
            # b번호 건물을 짓기 전에 먼저 지어야하는 선수 건물 짓는데 걸리는 시간으로 갱신
            result[b] = max(result[b], result[now])
            if indegree[b] == 0:
                q.append(b)

    return result


answer = topology_sort()
for i in range(1, N + 1):
    print(answer[i])








from collections import defaultdict, deque

n = int(input())
answer = [0] * (n + 1)
cost = [0] * (n + 1)
degree = [0] * (n + 1)
q = deque()
graph = defaultdict(list)

for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    cost[i] = temp[0]

    for element in temp[1:-1]:
        graph[element].append(i)
        degree[i] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)
        answer[i] = cost[i]

while q:
    now = q.popleft()
    for element in graph[now]:
        degree[element] -= 1
        answer[element] = max(answer[element], cost[element] + answer[now])

        if degree[element] == 0:
            q.append(element)

for i in range(1, n + 1):
    print(answer[i])