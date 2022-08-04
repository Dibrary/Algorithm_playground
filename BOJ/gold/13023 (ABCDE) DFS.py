
'''
핵심은 그래프의 깊이가 5임을 증명하기만 하면 된다.
'''
import sys

n, m = map(int, input().split())
arr = [[] for i in range(n)]
visited = [False] * n

# 그래프를 인접 리스트 방식으로 표현하였습니다.
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(idx, number):
    if number == 4:
        print(1)
        exit() # 이 코드를 쓰면 해당 부분에서 실행중인 모든 코드를 정지시켜버릴 수 있다.
    for i in arr[idx]:
        if not visited[i]:
            visited[i] = True # 방문 처리
            dfs(i, number + 1) # 재귀로 다시 한 단계 더 들어간다.
            visited[i] = False # 방문 처리를 원래대로 함.

# 노드를 순서대로 방문하며 dfs를 수행합니다.
for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)



## 다른 사람 코드 ##


from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
s = [[] for _ in range(n)]
visited = [False] * (n + 1)
ans = False
for i in range(m):
    a, b = map(int, input().split())
    s[a].append(b)
    s[b].append(a)

def dfs(idx, depth):
    global ans
    visited[idx] = True
    if depth == 4:
        ans = True
        return

    for i in s[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False

for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if ans:
        break

if ans:
    print(1)
else:
    print(0)











import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(number, count):
    if count == 4:
        print(1)
        sys.exit()

    for nxt in F[number]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, count + 1)
            visited[nxt] = False




N, M = map(int, input().split())
F = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    F[a].append(b)
    F[b].append(a)


for num in range(N):
    visited = [False] * N
    visited[num] = True
    dfs(num, 0)
print(0)

