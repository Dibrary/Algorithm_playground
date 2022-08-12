
'''
핵심 = 다리를 연결해서 모든 섬을 연결하려 한다.
다리의 길이는 2이상이어야 함.
다리의 방향은 중간에 바뀔 수 없다. (꺾이거나 하면 안 됨)
다리 끝은 섬과 수직으로 마주해야 한다.
교차할 경우 겹치는 부분은 '각각' 계산해 줘야 한다.


섬으로 표현된 값을 각각의 섬마다 다르게 표현해야 한다.
즉, 먼저 BFS를 통해 인접 지역은 같은 '숫자'로 인식해야 함.



'''


from collections import deque

n, m = map(int, input().split())
arr = []
visited = [[0 for _ in range(m)] for _ in range(m)]

for _ in range(n):
    arr.append(list(map(int, input().split())))

cnt = 1
def bfs(y, x):
    global cnt

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    q = deque()
    q.append((y, x))
    visited[y][x] = 1 # 방문처리
    arr[y][x] = cnt # 시작지점도 cnt로 바꿔주고,

    while q:
        print(q)
        y, x = q.popleft()
        for s in range(4):
            nx = x + dx[s]
            ny = y + dy[s]
            if nx < 0 or ny < 0 or ny >= len(arr) or nx >= len(arr[0]):
                continue
            if visited[ny][nx] == 0 and arr[ny][nx] == 1:
                arr[ny][nx] = cnt
                visited[ny][nx] = 1 # 여기서 방문처리 안하면 무한루프로 빠짐.
                q.append((ny, nx))


for k in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[k][j] == 1 and visited[k][j] == 0:
            bfs(k, j)
            cnt += 1

# 위 코드 까지 진행하면 각 섬을 1부터 순서대로 만들 수 있다.
# 여기서부터 어떻게 진행해야 할 지 감이 안잡힘.

















## 다른 사람 코드 ##
import sys
from collections import deque

r, c = map(int, sys.stdin.readline().rsplit())
islands = [[0 for _ in range(c)] for _ in range(r)]
arr = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(r)]

edges = []
cordis = []


def isin(y, x):
    if -1 < y < r and -1 < x < c: return True
    return False

d = ((0, 1), (0, -1), (1, 0), (-1, 0))
def _make_islands(visited, sy, sx, k): # BFS 과정.
    q = deque()
    q.append((sy, sx))

    while q:
        y, x = q.popleft()
        for dy, dx in d: # 이동방향은 d에 정의됨.
            ny = y + dy
            nx = x + dx
            if not isin(ny, nx): # 경계조건을 함수로 뺌.
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = True
                if arr[ny][nx] == 1:
                    islands[ny][nx] = k
                    q.append((ny, nx))
                    cordis.append((ny, nx, k))

def make_islands():
    visited = [[False for _ in range(c)] for _ in range(r)]
    k = 1
    for i in range(r):
        for j in range(c):
            if not visited[i][j] and arr[i][j] == 1:
                visited[i][j] = True
                islands[i][j] = k
                cordis.append((i, j, k))
                _make_islands(visited, i, j, k)
                k += 1
    return k


def _find_routes(sy, sx, k):
    q = deque()

    for dy, dx in d:
        q.append((sy, sx))
        visited = [[False for _ in range(c)] for _ in range(r)]
        visited[sy][sx] = True
        table = [[0 for _ in range(c)] for _ in range(r)]

        while q:
            y, x = q.popleft()
            ny = y + dy
            nx = x + dx

            if not isin(ny, nx):
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = True
                if islands[ny][nx] == 0:
                    table[ny][nx] = table[y][x] + 1
                    q.append((ny, nx))

                elif islands[ny][nx] != k and table[y][x] >= 2:
                    edges.append((table[y][x], k, islands[ny][nx]))


def find_routes():
    for y, x, k in cordis:
        _find_routes(y, x, k)

n = make_islands() - 1
find_routes()
uf = [-1 for _ in range(n + 1)]

def find(a):
    if uf[a] < 0:
        return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    uf[b] = a
    return True

edges.sort()
total, cnt = 0, 0

for w, a, b in edges:
    if merge(a, b):
        total += w
        cnt += 1
        if cnt == n - 1:
            break
if cnt == n - 1:
    print(total)
else:
    print(-1)









from collections import deque
import sys, heapq
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visit = [[False]*m for _ in range(n)]
move = [(0,1),(1,0),(0,-1),(-1,0)]
land = dict()
landArr = []

# 섬 구분하여 좌표 구하기, BFS
landNum = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visit[i][j]:
            q = deque([(i,j)])
            visit[i][j] = True
            land[(i,j)] = landNum
            landArr.append((i, j, landNum))

            while q:
                x, y = q.popleft()
                for a, b in move:
                    dx = x + a
                    dy = y + b
                    if n > dx >= 0 and m > dy >= 0 and not visit[dx][dy] and board[dx][dy]:
                        q.append((dx, dy))
                        visit[dx][dy] = True
                        land[(dx, dy)] = landNum
                        landArr.append((dx, dy, landNum))
            landNum += 1
# 다리 제작
edges = []
for x, y, curLand in landArr:
    for a, b in move:
        dist = 0
        dx = x + a
        dy = y + b
        while True:
            if n > dx >= 0 and m > dy >= 0:
                toLand = land.get((dx, dy))
                # 같은 섬
                if curLand == toLand:
                    break
                # 바다 위, 다리 길이 +1
                if toLand == None:
                    dx += a
                    dy += b
                    dist += 1
                    continue
                # 다리가 짧음
                if dist < 2:
                    break
                edges.append((dist, curLand, toLand))
                break
            else:
                break
edges = sorted(edges, reverse = True)

# 크루스칼 진행
def union(x,y):
    x = find(x)
    y = find(y)
    parents[y] = x

def find(k):
    if k != parents[k]:
        parents[k] = find(parents[k])
    return parents[k]

ans = 0
cnt = landNum - 1
parents = [i for i in range(landNum)]
while cnt:
    try:
        w, a, b = edges.pop()
    except:
        # empty list, 다리 부족
        print(-1)
        sys.exit()
    if find(a) != find(b):
        union(a, b)
        ans += w
        cnt -= 1
print(ans)












import sys
from collections import deque

# 생성 가능한 다리 찾기
def check(li):
    start, cnt = 0, 0
    flag = False
    for idx in range(len(li)):
        if li[idx] and not flag:
            flag = True
            start = li[idx]
        elif not li[idx] and flag:
            cnt += 1
        elif li[idx] and flag and start != li[idx]:
            if start and cnt >= 2:
                if (start, li[idx], cnt) not in edge:
                    edge.append((start, li[idx], cnt))
            cnt = 0
            start = li[idx]
        elif start == li[idx]:
            cnt = 0


N, M = map(int, input().split())
country = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = 1  # 섬 고유번호
used = []  # BFS 사용시 방문여부 판단
queue = deque([])  # BFS에서 사용하는 큐(queue)
edge = []  # 생성가능한 다리 후보를 담는 배열

# BFS를 이용하여 섬 고유번호 붙이기
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(N):
    for j in range(M):
        if country[i][j] and (i, j) not in used:
            queue.append((i, j))
            used.append((i, j))

            while queue:
                r, c = queue.popleft()
                country[r][c] = cnt
                for idx in range(4):
                    nr = r + direction[idx][0]
                    nc = c + direction[idx][1]
                    if 0 <= nr < N and 0 <= nc < M:
                        if country[nr][nc] and (nr, nc) not in used:
                            queue.append((nr, nc))
                            used.append((nr, nc))
            cnt += 1

# 행 탐색
for row in country:
    if sum(row):
        check(row)

# 열 탐색
for col in list(zip(*country)):
    if sum(col):
        check(col)

# 크루스칼(Kruskal) 알고리즘 부분
edge = sorted(edge, key=lambda x: [x[2]])

parents = [i for i in range(cnt)]
rank = [1 for i in range(cnt)]

# 부모를 찾는 함수
def find(v):
    if v != parents[v]:
        parents[v] = find(parents[v])
    return parents[v]

answer = 0

# 합치는 함수(grouping)
def union(v1, v2, w):
    global answer
    root1, root2 = find(v1), find(v2)

    if root1 != root2:
        answer += w

        if rank[root1] < rank[root2]:
            rank[root2] += rank[root1]
            parents[root1] = root2
        else:
            rank[root1] += rank[root2]
            parents[root2] = root1

for e in edge:
    union(e[0], e[1], e[2])

if max(rank) != cnt - 1:
    print(-1)
else:
    print(answer)





# 최소신장트리 사용 코드
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def DFS(i, j, country):
    if i <= -1 or i >= len(arr) or j <= -1 or j >= len(arr[0]):
        return 0
    if visit[i][j] == 0 and arr[i][j]:
        visit[i][j] = country
        ctry_coord.append((i, j, country))
        for k in range(4):
            nx, ny = i+dx[k], j+dy[k]
            DFS(nx, ny, country)
    return 0

def distance():
    for coord in ctry_coord:
        i, j, country_num = coord
        for k in range(4):
            dist = 0
            nx, ny = i+dx[k], j+dy[k]

            while True:
                if nx <= -1 or nx >= len(visit) or ny <= -1 or ny >= len(visit[0]):
                    break
                else:
                    if country_num == visit[nx][ny]:
                        break
                    if visit[nx][ny] == 0:
                        nx, ny = nx+dx[k], ny+dy[k]
                        dist += 1
                        continue
                    if dist < 2:
                        break
                    edges.append((dist, country_num, visit[nx][ny]))
                    break

def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]

def union(p, a, b):
    a, b = find(p, a), find(p, b)
    p[max(a, b)] = min(a, b)

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

visit = [[0]*m for i in range(n)]
country = 0
ctry_coord = []
edges = []
res = 0

for i in range(n):
    for j in range(m):
        if not visit[i][j] and arr[i][j] == 1:
            country += 1
            DFS(i, j, country)

p = [i for i in range(country+1)]

distance()
edges.sort()
cnt = 0

for edge in edges:
    c, a, b = edge
    if find(p, a) != find(p, b):
        union(p, a, b)
        res += c
        cnt += 1

if cnt == country - 1:
    print(res)
else:
    print(-1)



