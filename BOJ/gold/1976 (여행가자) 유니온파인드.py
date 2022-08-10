
'''
그래프가 인접행렬 꼴로 주어짐.

union - find 연산으로 주어짐

같은 root를 가지고 있다면 방문할 수 있는 셈이 된다.
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(a):
    if a == parent[a]:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a > b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())

parent = [x for x in range(n+1)]

for i in range(n):
    tmp = list(map(int, input().split()))
    for idx, x in enumerate(tmp):
        if x != 0:
            union(i+1, idx+1) # 도시는 1부터라서 +1을 해 줌.

arr = list(map(int, input().split()))

result = set()
for k in arr:
    result.add(find(k))

if len(result) == 1:
    print("YES")
else:
    print("NO")

# find와 union 함수만 알고 있으면 금방 푸는 문제다.


## 다른 사람 코드 ##

import sys
input = sys.stdin.readline

def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
    return parent[n]

def union(x, y):
    x = find(x)
    y = find(y)
    parent[y] = x

N = int(input())
M = int(input())
parent = list(range(N + 1))

for i in range(1, N + 1):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j]:
            union(i, j + 1)

plans = list(map(int, input().split()))
ans = set([find(p) for p in plans])

if len(ans) == 1:
    print('YES')
else:
    print('NO')








import sys
f = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b
    else:
        return

n = int(f())
m = int(f())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(1, n+1):
    graph = list(map(int, f().split()))
    for j in range(1, len(graph)+1):
        if graph[j-1] == 1:
            union_parent(parent, i, j)

candidate_list = list(map(int, f().split()))
result = []
for i in candidate_list:
    result.append(find_parent(parent, i))

if len(set(result)) == 1:
    print("YES")
else:
    print("NO")







