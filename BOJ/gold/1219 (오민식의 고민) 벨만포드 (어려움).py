
'''
벨만-포드 알고리즘은 최단거리를 구하는 알고리즘이지만,
도착하는 도시에서 돈 액수를 최대로 하려면 업데이트 방식을 반대로 변경해야 한다.

돈을 무한히 많이 버는 케이스가 있다고 하는 것을 바탕으로 음수 사이클이 아닌 양수 사이클을 찾도록 변경해야 한다.

그리고, 예외상황은, 출발노드에서 양수사이클을 이용해 도착 도시에 가지 못할 경우가 있다.

'''


n, start, end, m = map(int, input().split())
MIN = -10e9

edges = []
dist = [0]+[MIN for _ in range(1, n)] # 모든 거리 최소값으로 세팅


for _ in range(m):
    s, e, price = map(int, input().split())
    edges.append((s, e, price)) # s에서 e로 가는데 price 듦.

money = list(map(int, input().split()))


def bellman_ford(start):
    visited = [False] * (n)

    for i in range(n + 10):
        for j in range(m):
            start = edges[j][0]
            end = edges[j][1]
            price = edges[j][2]


bellman_ford(start)




## 다른 사람 코드 ##
def check(E):
    visit = [0] * N
    q = [E]
    while q:
        a = q.pop()
        if a == End:
            return True
        visit[a] = 1
        for b, c in network[a]:
            if visit[b] == 0:
                q.append(b)
    return False

def BF():
    for i in range(N+1):
        if sections[End] == -float('inf') and i == N:
            print('gg')
            return
        for j in range(N):
            if sections[j] == -float('inf'):
                continue
            for E, T in network[j]:
                if sections[j] + T > sections[E]:
                    sections[E] = sections[j] + T
                    if i == N:
                        if check(E):
                            print('Gee')
                            return False
    return True

N, Start, End, M = map(int, input().split())
sections = [-float('inf')] * N
network = [[] for i in range(N)]

for i in range(M):
    S, E, T = map(int, input().split())
    network[S].append([E, T])

salary = list(map(int, input().split()))
sections[Start] = salary[Start]

for i in range(len(salary)):
    for j in range(len(network[i])):
        for k in range(len(salary)):
            if network[i][j][0] == k:
                network[i][j][1] = salary[k] - network[i][j][1]

if BF():
    print(sections[End])










import sys
from collections import deque

def can_reach(start, end):
    q = deque()
    q.appendleft(start)

    vis = [False for i in range(N)]

    while len(q) != 0:
        here = q.pop()

        if here == end:
            return True

        for there, here2there in edge[here]:
            if vis[there] == False:
                q.appendleft(there)
                vis[there] = True

    return False

def bellman_ford(start):
    upper = [sys.maxsize for i in range(N)]

    upper[start] = -earnedMoney[start]

    for i in range(N - 1):
        for here in range(N):
            for there, here2there in edge[here]:
                if upper[here] != sys.maxsize and upper[there] > upper[here] + here2there - earnedMoney[there]:
                    upper[there] = upper[here] + here2there - earnedMoney[there]

    for here in range(N):
        for there, here2there in edge[here]:
            if upper[here] != sys.maxsize and upper[there] > upper[here] + here2there - earnedMoney[there]:
                if can_reach(here, E):
                    return "Gee"

    return -upper[E] if upper[E] != sys.maxsize else "gg"


N, S, E, M = map(int, input().split())

edge = [[] for i in range(N)]
for i in range(M):
    s, e, w = map(int, input().split())
    edge[s].append((e, w))

earnedMoney = list(map(int, input().split()))

reachable = [[False for i in range(N)] for i in range(N)]

print(bellman_ford(S))









import sys

def dfs(next):
    visited = [0] * n
    q = [next]
    while q:
        x = q.pop()
        # next에서 시작해 end로 돌아갈 수 있는 경우 계속 이익을 얻으며 돌 수 있음
        if x == end:
            return True
        visited[x] = 1
        for b, c in edges[x]:
            if not visited[b]:
                q.append(b)
    return False

def bellman_ford():
    dist[start] = gain[start]
    for i in range(n+1):
        # end에 방문하지 못하는 경우
        if dist[end] == -sys.maxsize and i == n:
            print('gg')
            return False
        for now in range(n):
            for next, ni in edges[now]:
                if dist[now] != -sys.maxsize and dist[next] < dist[now] + ni:
                    dist[next] = dist[now] + ni
                    if i == n:
                        if dfs(next):
                            print('Gee')
                            return False
    return True


input = sys.stdin.readline

n, start, end, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
gain = list(map(int, input().split()))

dist = [-sys.maxsize] * n
# edges의 cost를 gain-cost로 바꾸기
for i in range(n):
    for j in range(len(edges[i])):
        for k in range(n):
            if edges[i][j][0] == k:
                edges[i][j][1] = gain[k] - edges[i][j][1]

if bellman_ford():
    print(dist[end])


























