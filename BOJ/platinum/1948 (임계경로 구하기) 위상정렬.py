
'''
출발 도시로부터 최소 몇 시간 후에 만날 수 있는가. 이게 진짜 질문.
1분도 쉬지 않고 달려야 하는 도로(임계경로)의 갯수. 이게 진짜 질문.

에지 뒤집기 라는 개념이 필요. 역추적을 하는 것이다.
'''

# from collections import deque
#
# n = int(input())
# m = int(input())
#
# orders = [0 for _ in range(n+1)] # 진입차수
# table = [[0 for _ in range(n+1)] for _ in range(n+1)] # 연결된 곳 hour정보
#
# reverse_orders = [0 for _ in range(n+1)] # 역방향 진입차수
# reverse_table = [[0 for _ in range(n+1)] for _ in range(n+1)] # 역방향 연결된 곳 hour정보
#
# for _ in range(m):
#     start, end, hour = map(int, input().split())
#     orders[end] += 1
#     table[start][end] = hour
#     reverse_orders[start] += 1
#     reverse_table[end][start] = hour
#
# start, end = map(int, input().split()) # 출발도시, 도착도시
#
# result_1 = [0 for _ in range(n+1)]
#
# q = deque()
#
# for idx, v in enumerate(orders[1:]):
#     if v == 0:
#         q.append(idx) # 진입점이 0인 것의 index넣음
#         orders[idx] = -1
#
# while q:
#     node = q.popleft()
#     for idx, x in enumerate(table[node]):
#         result_1[idx] = x + orders[idx]
#         if orders[idx] > 0:
#             orders[idx] -= 1
#         if orders[idx] == 0:
#             q.append(idx)
#             orders[idx] = -1
# print(result_1)








## 다른 사람 코드 ##
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n+1)]
nodes_inv = [[] for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]

for _ in range(m):
    tail, head, cost = map(int, sys.stdin.readline().rstrip().split())
    nodes[tail].append([head, cost])
    in_degree[head] += 1
    nodes_inv[head].append([tail, cost])

start, end = map(int, sys.stdin.readline().rstrip().split())

def topological_sort():
    queue = deque()
    dp = [0 for i in range(n+1)]
    for i in range(1, n+1):
        if in_degree[i] == 0:
            queue.append([i, 0])

    while queue:
        cur_node, cur_cost = queue.popleft()

        for next_node, next_cost in nodes[cur_node]:
            in_degree[next_node] -= 1
            dp[next_node] = max(dp[next_node], next_cost + dp[cur_node])
            if in_degree[next_node] == 0:
                queue.append([next_node, cur_cost + next_cost])

    return dp
# 위상 정렬을 dp를 통해 값을 누적시키면서 정렬. 각 도시별로 가는 최장 거리를 기록한다.

dp = topological_sort()

edges = set()
def BFS():
    queue = deque()
    queue.append([end, 0])
    # nodes_inv는 그래프의 head와 tail을 거꾸로 만든 그래프

    while queue:
        cur_node, cur_cost = queue.popleft()

        for post_node, post_cost in nodes_inv[cur_node]:
            if dp[cur_node] == post_cost + dp[post_node] and tuple((post_node, cur_node)) not in edges:
                # post_cost를 사용한 루트가 최장 거리일 때에만 추적한다. 이때 중복 간선을 체크하기 위해 set으로 확인.
                edges.add(tuple((post_node, cur_node)))
                queue.append([post_node, cur_cost+post_cost])
BFS()

print(dp[end])
# end까지 간선으로 이동하는 최장 거리
print(len(edges))
# 최장거리 루트에 사용된 간선의 개수










import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, M = int(input()), int(input())
L, L_reverse = defaultdict(list), defaultdict(list)
C = [0] * (N + 1)
for i in range(M):
    a, b, c = map(int, input().split())
    L[a].append((b, c))
    L_reverse[b].append((a, c))
    C[b] += 1
start, end = map(int, input().split())

Q = deque()
Q.append((0, start))

D = [0] * (N + 1)
while Q:
    SD, SN = Q.popleft()

    for FN, FD in L[SN]:
        C[FN] -= 1
        D[FN] = max(D[FN], SD + FD)
        if not C[FN]:
            Q.append((D[FN], FN))

Q = deque()
Q.append(end)

V = defaultdict(int)
V[end] = 1

count = 0
while Q:
    SN = Q.popleft()

    for FN, FD in L_reverse[SN]:
        if FD + D[FN] == D[SN]:
            count += 1
            if not V[FN]:
                Q.append(FN)
                V[FN] = 1

print(D[end])
print(count)











import sys
from collections import deque

input = sys.stdin.readline

n = int(input()) #노드, 도시 개수
m = int(input()) #도로의 개수
graph = [[]*(n+1) for _ in range(n+1)]
back_graph = [[]*(n+1) for _ in range(n+1)]
indegree = [0]*(n+1) #진입차수
result = [0]*(n+1)
check = [0]*(n+1)
q = deque()

for _ in range(m):
    a, b, t = map(int,input().split())
    graph[a].append((b,t))
    back_graph[b].append((a,t))
    indegree[b] += 1
start, end = map(int,input().split())

q.append(start)

def topologysort():
    while q:
        cur = q.popleft()
        for i, t in graph[cur]:
            indegree[i] -= 1
            result[i] = max(result[i], result[cur] + t)
            if indegree[i] == 0:
                q.append(i)

    #백트래킹
    cnt = 0 #임계경로에 속한 모든 정점의 개수
    q.append(end)
    while q: #도착점에서 시작점으로
        cur = q.popleft()
        for i, t in back_graph[cur]:
            #도착점까지의 비용에서 시작점의 비용을 뺐을 때 그 간선비용과 같다면
            if result[cur] - result[i] == t:
                cnt += 1
                if check[i] == 0: #큐에 한번씩만 담을 수 있도록,중복방문제거
                    q.append(i)
                    check[i] = 1

    print(result[end])
    print(cnt)

topologysort()









import sys
from collections import deque

input = sys.stdin.readline

N = int(input())    # N: 도시의 개수
M = int(input())    # M: 도로의 개수

time = [0] * (N+1)
in_degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
bgraph = [[] for _ in range(N+1)]    # backward of graph
cnt = [[] for _ in range(N+1)]

for _ in range(M):
    # a: 출발 도시, b: 도착 도시, c: 걸리는 시간
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    bgraph[b].append(a)
    in_degree[b] += 1

src, dst = map(int, input().split())

q = deque([])
# 도시, 지나온 경로 개수
q.append(src)

while q:
    # now: 도시, c: 지나온 경로의 개수
    now = q.popleft()
    # i[0]: 비용, i[1]: 도시
    for i in graph[now]:
        in_degree[i[1]] -= 1
        # 비용이 갱신 될 때
        if time[i[1]] < time[now] + i[0]:
            time[i[1]] = time[now] + i[0]
            # 달려야 하는 도로의 수 갱신
            cnt[i[1]] = [now]
        elif time[i[1]] == time[now] + i[0]:
            cnt[i[1]].append(now)

        # 선행 도로를 모두 지나갔을 때
        if in_degree[i[1]] == 0:
            q.append(i[1])

q = deque([dst])
route = set()
while q:
    now = q.popleft()
    for x in cnt[now]:
        if (now, x) not in route:
            route.add((now, x))
            q.append(x)

print(time[dst])
print(len(route))

