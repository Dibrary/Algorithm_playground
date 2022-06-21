
# 먼저 든 생각은 들어있는 값을 하나씩 만 저장한 별개의 객체를 두고
# 해당 객체일 때 최대 값을 구한다.
import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

n = int(input())

ground = []
for _ in range(n):
    ground.append(list(map(int, input().split())))

tmp = set()
for k in ground:
    for j in k:
        tmp.add(j)

def dfs(y, x, target):
    if y<0 or x<0 or (y>=len(ground)) or (x>=len(ground[0])) or (visited[y][x] == 1) or (ground[y][x] < target):
        return False
    visited[y][x] = 1
    dfs(y-1, x, target)
    dfs(y, x-1, target)
    dfs(y+1, x, target)
    dfs(y, x+1, target)
    return True

max_value = 0

for k in tmp:
    visited = [[0 for _ in range(len(ground[0]))] for _ in range(len(ground))]
    cnt = 0
    for i in range(len(ground)):
        for j in range(len(ground[0])):
            if visited[i][j] == 0 and ground[i][j] == k:
                if dfs(i, j, k):
                    cnt += 1
    if cnt >= max_value:
        max_value = cnt

print(max_value)

# 5%에서 틀림, 2번째 예제 답이 제대로 나오지 않음.


n = int(input())

ground = []
for _ in range(n):
    ground.append(list(map(int, input().split())))

tmp = set()
for k in ground:
    for j in k:
        tmp.add(j)

def dfs(y, x, target):
    if y<0 or x<0 or (y>=len(ground)) or (x>=len(ground[0])) or (visited[y][x] == 1) or (ground[y][x] <= target): # 같은 경우도 침수된다고 해야 함.
        return False
    visited[y][x] = 1
    dfs(y-1, x, target)
    dfs(y, x-1, target)
    dfs(y+1, x, target)
    dfs(y, x+1, target)
    return True

max_value = 0

for k in tmp:
    visited = [[0 for _ in range(len(ground[0]))] for _ in range(len(ground))]
    cnt = 0
    for i in range(len(ground)):
        for j in range(len(ground[0])):
            if visited[i][j] == 0 and ground[i][j] != k: # k랑 다를 때 진입해야 한다.
                if dfs(i, j, k):
                    cnt += 1
    if cnt >= max_value:
        max_value = cnt

print(max_value)

# 88%에서 틀림


