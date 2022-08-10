
'''
그래프를 역으로 그리는 방식 문제.
A,B,C의 특정 무게 상태를 1개의 노드로 가정하고,
조건에 따라 이 상태에서 변경할 수 있는 이후 무게 상태가 에지로 이어진 인접 노드라고 간주하자.

물을 옮길 수 있는 방법의 수는 6가지.

'''

from collections import deque

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        pass

a, b, c = map(int, input().split())

result = set()




## 다른 사람 코드 ##
import sys
from collections import deque

# x, y의 경우의 수 저장
def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))

def bfs():

    while q:
        # x : a물통의 물의 양, y : b물통의 물의 양, z : c물통의 물의 양
        x, y = q.popleft()
        z = c - x - y

        # a 물통이 비어있는 경우 c 물통에 남아있는 양 저장
        if x == 0:
            answer.append(z)

        # x -> y
        water = min(x, b-y)
        pour(x - water, y + water)
        # x -> z
        water = min(x, c-z)
        pour(x - water, y)
        # y -> x
        water = min(y, a-x)
        pour(x + water, y - water)
        # y -> z
        water = min(y, c-z)
        pour(x, y - water)
        # z -> x
        water = min(z, a-x)
        pour(x + water, y)
        # z -> y
        water = min(z, b-y)
        pour(x, y + water)


# 입력(리터 범위)
a, b, c = map(int, sys.stdin.readline().split())

# 경우의 수를 담을 큐
q = deque()
q.append((0, 0))

# 방문 여부(visited[x][y])
visited = [[False] * (b+1) for _ in range(a+1)]
visited[0][0] = True

# 답을 저장할 배열
answer = []

bfs()

# 출력
answer.sort()
for i in answer:
    print(i, end=" ")










from collections import deque

x, y, z = map(int, input().split())
maximum_water = [x, y, z]
visit = [[False] * (x + 1) for _ in range(y + 1)]
ans = set()
q = deque()


def move(c, move_from, move_to):
    next_c = c.copy()
    next_c[move_to] = min(c[move_to] + c[move_from], maximum_water[move_to])
    next_c[move_from] = c[move_from] - min(maximum_water[move_to] - c[move_to], c[move_from])
    return next_c


q.append([0, 0, z])
visit[0][0] = True
while q:
    current = q.popleft()
    if current[0] == 0:
        ans.add(current[2])
    for i in range(0, 3):
        for j in range(0, 3):
            next_water = move(current, i, j)
            if i != j and not visit[next_water[1]][next_water[0]]:
                q.append(next_water)
                visit[next_water[1]][next_water[0]] = True

print(" ".join(map(str, sorted(ans))))







from collections import deque
a, b, c = map(int,input().split())
lim = (a, b, c)
volume = set([(0, 0, c)])
c_vol = set([(c)])
q = deque([(0, 0, c)])

def move(x,y,cur,lim=lim):
    if not cur[x]:
        return None
    ret = list(cur)

    if lim[y] - cur[y] >= cur[x]:
        ret[y] += ret[x]
        ret[x] = 0
    else:
        ret[x] -= lim[y] - ret[y]
        ret[y] = lim[y]
    ret = tuple(ret)

    if ret not in volume:
        if not ret[0]:
            c_vol.add(ret[2])
        volume.add(ret)
        q.append(ret)
    return ret

while q:
    cur = q.popleft()
    move(0, 1, cur)
    move(1, 0, cur)
    move(0, 2, cur)
    move(2, 0, cur)
    move(1, 2, cur)
    move(2, 1, cur)
c_vol = list(c_vol)
c_vol.sort()

for i in c_vol:
    print(i, end=' ')








