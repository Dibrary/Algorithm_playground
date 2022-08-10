

def find(node):
    low_value = 10e9
    while low_value != node:
        if nodes[node] <= low_value:
            low_value = nodes[node]
            node = nodes[node] # 여기서 어떻게 해야 할 지 모르겠음.

def union(a, b):
    if b != a:
        nodes[b] = a # a값을 넣고
        find(b) # b의 꼭대기를 find한다.

n, m = map(int, input().split())

for _ in range(m):
    nodes = [k for k in range(n+1)] # 처음에 숫자 값을 그대로 넣어만든다.

    s, a, b = map(int, input().split()) # s값이 0이면 집합 구성. 1이면 a가 b에 속하는지 확인하는 용도다.
    if s == 0:
        union(a, b)
    elif s == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")




## 다른 사람 코드 ##

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int,input().split())

parent = [0] * (N+1) # 부모 테이블 생성
for i in range(N+1): # 자기 자신을 부모로 설정
    parent[i] = i

# 루트 노드 찾는 함수
def find(a):
    if a == parent[a]: # 자기 자신이 루트 노드이면 a 반환
        return a
    p = find(parent[a]) # a의 루트 노드 찾기
    parent[a] = p # 부모 테이블 갱신
    return parent[a] # a의 루트 노드 반환

# a가 속해있는 집합과 b가 속해있는 집합을 합치는 연산
def union(a,b):
    a = find(a) # a의 루트 노드 찾기
    b = find(b) # b의 루트 노드 찾기

    if a == b: # a와 b의 루트 노드가 같으면 동일한 집합
        return
    if a < b: # a와 b의 루트 노드가 다르면 두 집합을 합치기
        parent[b] = a
    else:
        parent[a] = b

for _ in range(M):
    o, a, b = map(int,input().split()) # operation, 원소, 원소
    if o == 0: # o=0은 두 원소가 포함되어 있는 집합을 합치기
        union(a,b)
    elif o == 1: # 두 원소가 동일한 집합인지 판단
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')








import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


# 재귀를 활용해서 최종 부모까지 찾기
def find_parent(parent, k):
    if k != parent[k]:
        parent[k] = find_parent(parent, parent[k])
    return parent[k]


# unionfind 찾아서 조합하는건데 작은 쪽으로 연결 시켜줌
def union_find(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
for _ in range(m):
    z, a, b = map(int, input().split())
    if z == 0:
        union_find(parent, a, b)
    else:
        # 최종 같은 부모면 YES 아니면 NO
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
print(parent)










import sys
def union(a,b):
    A = find_root(a)
    B = find_root(b)
    if depth[A] > depth[B]:
        group[B] = A
    elif depth[A] < depth[B]:
        group[A] = B
    else:
        group[A] = B
        depth[B] += 1

def find_root(n):
    if group[n] == n:
        return n
    group[n] = find_root(group[n])
    return group[n]


n,m = map(int,sys.stdin.readline().split())
group = [num for num in range(n+1)]
depth = [1]*(n+1)
for _ in range(m):
    F,a,b = map(int,sys.stdin.readline().split())
    if F == 0:
        union(a,b)
    else:
        if find_root(a) == find_root(b):
            print("YES")
        else:
            print("NO")