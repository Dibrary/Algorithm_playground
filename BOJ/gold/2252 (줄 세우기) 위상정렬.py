
'''
위상정렬 = 사이클이 없는 방향그래프에서 노드 순서를 찾는 알고리즘.

노드가 지워지면 연결된 각 노드별로 진입 가능한 차수가 줄어든다.

위상정렬은 항상 같은 값이 나온다는 보장은 없다. 지워지는 순서가 항상 같지 않을 수 있음.

'''

# from collections import deque
#
# n, m = map(int, input().split())
#
# orders = [0 for k in range(n+1)]
# table = dict()
#
# for _ in range(m):
#     a, b = map(int, input().split()) # a가 b를 가리킨다고 하자.
#     orders[b] += 1
#
#     if a not in table:
#         table[a] = [b]
#     else:
#         table[a].append(b)
#
# result = []
# q = deque()
# for idx, m in enumerate(orders):
#     if m == 0 and idx != 0: # 시작부분을 모두 큐에 넣는다.
#         q.append(idx)
# while q:
#     node = q.popleft()
#     result.append(node)
#     for x in table[node]:
#         if orders[x] != 0:
#             orders[x] -= 1
#         if orders[x] == 0:
#             q.append(x)

# 위 코드로 하면 맨 마지막 노드 값이 들어가지 않는다.

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

orders = [0 for k in range(n+1)]
table = dict()

for _ in range(m):
    a, b = map(int, input().split()) # a가 b를 가리킨다고 하자.
    orders[b] += 1

    if a not in table:
        table[a] = [b]
    else:
        table[a].append(b)

result = []
q = deque()
for idx, m in enumerate(orders):
    if m == 0 and idx != 0: # 시작부분을 모두 큐에 넣는다.
        q.append(idx)
while q:
    node = q.popleft()
    result.append(node)

    if node not in table:
        pass
    else:
        for x in table[node]:
            if orders[x] != 0:
                orders[x] -= 1
            if orders[x] == 0:
                q.append(x)
print(" ".join(map(str, result)))


## 다른 사람 코드 ##

import sys

input = sys.stdin.readline
from collections import deque


def topology():
    dq = deque()

    for i in range(1, n + 1):
        if degrees[i] == 0:
            dq.append(i)

    while dq:
        t = dq.popleft()
        print(t, end=' ')
        for cv in graph[t]:
            degrees[cv] -= 1
            if degrees[cv] == 0:
                dq.append(cv)


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    degrees = [0] * (n + 1)

    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)
        degrees[e] += 1

    topology()







from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
cnt = [0] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    cnt[b] += 1

q = deque()
for i in range(1,N+1):
    if cnt[i] == 0:
        q.append(i)

while q:
    num = q.popleft()

    for number in graph[num]:
        cnt[number] -= 1
        if cnt[number] == 0:
            q.append(number)

    print(num,end=' ')








N, M = map(int, input().split())
N += 1

E = [[]for _ in range(N)]
C = [0]*N
D = []
for _ in range(M):
    a, b = map(int, input().split())
    E[b] += [a]
    C[a] += 1

for i in range(1, N):
    if C[i] < 1:
        D += [i]
for u in D:
    for v in E[u]:
        C[v] -= 1
        if C[v] == 0:
            D += [v]

print(*D[::-1])








from collections import deque
import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

less_list = (N+1) * [0]
graph = dict()

for i in range(M):
    s, e = list(map(int, input().split()))
    if s in graph.keys():
        graph[s].append(e)
    else:
        graph[s] = [e]
    less_list[e] += 1

q = []

for i in range(1, N+1):
    if less_list[i] == 0:
        q.append(i)

answer = []

while q:
    top = q.pop()
    answer.append(str(top))

    if top not in graph.keys():
        continue

    for node in graph[top]:
        less_list[node] -= 1
        if less_list[node] == 0:
            q.append(node)

print(' '.join(answer))
