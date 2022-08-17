
'''
ord('a') 하면 97 나온다.
즉 ord('a')-96 = 1이 된다.

ord('A') 하면 65 나온다.

이 문제의 핵심은 입력을 최소 신장 트리 알고리즘을 쓸 수 있는 형태로 변형하는 것이다.

예제에서 입력이
1, 2, 3
4, 5, 6
7, 8, 9 로 주어질 때,

1에서 1로 가는건 의미 없고, 1에서 2로 가는 경우는 2, 1에서 3으로 가는 경우는 3
2에서 1로 가는 경우는 4, 2에서 2로 가는건 의미 없고, 2에서 3으로 가는 경우는 6
3에서 1로 가는 경우는 7, 3에서 2로 가는 경우는 8, 3에서 3으로 가는건 의미 없다.

그래서, 엣지 리스트는
1 2 2
1 3 3
2 1 4
2 3 6
3 1 7
3 2 8 이 된다.

'''


# n = int(input())
#
# arr = []
# for _ in range(n):
#     # values = list(map(int, input().split()))
#     # if len(values) == 3:
#     #     start, end, begin = values[0], values[1], values[2]
#     # else: # 하나가 0인 경우다.
#     #     pass # 진입점이 0인 경우는 어떻게 처리해야 하나?
#
#     arr.append(list(input())) # 입력을 곧바로 리스트에 담아보는 것이다.

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(input())) # 입력을 곧바로 리스트에 담아보는 것이다.

total_value = 0
edge_list = []

for y in range(len(arr)):
    for x in range(len(arr[0])):
        k = arr[y][x]
        tmp = None
        if x == y:
            if k.isupper():
                tmp = (ord(k)-38)
            elif k.islower():
                tmp = (ord(k)-96)
            elif k == '0':
                tmp = 0
            total_value += int(tmp)
            continue
        else:
            if k.isupper():
                tmp = (ord(k)-38)
            elif k.islower():
                tmp = (ord(k)-96)
            elif k == '0':
                continue
            total_value += int(tmp)
            edge_list.append((y+1, x+1, tmp))

# print(edge_list, total_value) # [(1, 2, 2), (1, 3, 3), (2, 1, 4), (2, 3, 6), (3, 1, 7), (3, 2, 8)] 로 나온다.
parent = [i for i in range(n+1)]

def findParent(parent, x):
    if parent[x] != x:
        return findParent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

ans = 0
for a, b, w in edge_list:
    if findParent(parent, a) != findParent(parent, b):
        union(parent, a, b)
        ans += w

if edge_list == []:
    print(-1)
else:
    print(total_value - ans)

# 위 코드는 예제 3번까지만 맞고, 4,5는 안맞는다.






## 다른 사람 코드 ##

def make_egdes():
    total_weight = 0
    for i in range(N):
        row = input()
        for j in range(N):
            if ord('a') <= ord(row[j]) <= ord('z'):
                weight = ord(row[j]) - ord('a') + 1
            elif ord('A') <= ord(row[j]) <= ord('Z'):
                weight = ord(row[j]) - ord('A') + 27
            else:
                weight = 0

            if weight != 0:
                edges.append((weight, i, j))
                total_weight += weight
    return total_weight


def make_roots():
    for i in range(N):
        roots[i] = i
        sizes[i] = 1


def find_root(v):
    # if v != roots[v]:
    #     return find_root(roots[v])
    # return roots[v]
    while v != roots[v]:
        v = roots[v]
    return roots[v]


def union(v_root, u_root):
    if sizes[v_root] < sizes[u_root]:
        roots[v_root] = u_root
        sizes[u_root] += sizes[v_root]
    else:
        roots[u_root] = v_root
        sizes[v_root] += sizes[u_root]


def kruskal():
    minimum_spanning_tree = []

    # 각 정점을 독립 집합화 하고
    make_roots()

    # 엣지를 오름차순 정렬하고
    sorted_edges = sorted(edges, key = lambda edge: edge[0])

    for edge in sorted_edges:
        # 최소 엣지의 양끝노드를 꺼내서
        weight, v, u = edge

        # 루트가 다르면
        v_root         = find_root(v)
        u_root = find_root(u)

        if v_root != u_root:
            # 합친다
            union(v_root, u_root)
            # 그리고 mst에 추가한다
            minimum_spanning_tree.append(edge)

        # mst의 크기가 N-1이면 종료
        if len(minimum_spanning_tree) == N-1:
            break

    if len(minimum_spanning_tree) < N-1: # 트리가 만들어지지 않음
        return -1
    else:
        return minimum_spanning_tree


N = int(input())

roots = {}
sizes = {}
edges = []

total_weight = make_egdes() # egdes 채우고 가진 랜선길이 return
mst = kruskal()

if mst == -1:
    print(mst)
else:
    sum = 0
    for edge in mst:
        sum += edge[0]

    print(total_weight - sum)









import sys
import heapq
import string

n = int(sys.stdin.readline().rstrip())
letter_code = {letter:idx for idx, letter in enumerate(string.ascii_letters, start=1)}
parents = [i for i in range(n)]
pq = []
base = 0

for i in range(n):
    line = sys.stdin.readline().rstrip()
    for j in range(n):
        if line[j] != '0':
            base += letter_code.get(line[j])
            heapq.heappush(pq, [letter_code.get(line[j]), i, j])

def find(node):
    if parents[node] == node:
        return node
    else:
        parents[node] = find(parents[node])
        return parents[node]

def union(node1, node2):
    root1, root2 = find(node1), find(node2)
    if root1 == root2:
        return False
    else:
        parents[root2] = root1
        return True

total = 0
edge_num = 0
while pq:
    cur_cost, node1, node2 = heapq.heappop(pq)
    if union(node1, node2):
        total += cur_cost
        edge_num += 1
        if edge_num == n-1:
            break

if edge_num == n-1:
    print(base - total)
else:
    print(-1)








import sys
input = sys.stdin.readline
import heapq

# 숫자로 변경
def remote(s):
    if s == '0':
        return 0
    if s.isupper():
        return ord(s) - ord('A') + 27
    else:
        return ord(s) - ord('a') + 1

# mst 알고리즘

# 분리집합 클래스
class DisjointSet:
    def __init__(self):
        self.parent = None

# 합집합 연산
def unionset(set1, set2):
    set2 = findset(set2)
    set2.parent = set1

# 분리집합 부모 찾
def findset(s):
    while s.parent != None:
        s = s.parent
    return s

def kruskal(n, weight):
    vertex_set = [DisjointSet() for _ in range(n)]  # 부분 집합
    heap = []

    for i in range(n):
        for j in range(n):
            if i != j and weight[i][j] > 0:
                heapq.heappush(heap, (weight[i][j], i, j))
    cnt = 1
    weight_sum = 0
    while heap:
        w, v1, v2 = heapq.heappop(heap)
        set1 = vertex_set[v1]  # 집합
        set2 = vertex_set[v2]  # 집합

        if findset(set1) != findset(set2):
            unionset(set1, set2)  # 합집합 해줌
            weight_sum += w
            cnt += 1

    return weight_sum if cnt == n else -1

if __name__ == "__main__":
    n = int(input())
    weight = [[0] * n for _ in range(n)]
    for i in range(n):
        tmp = input().strip()
        for j in range(n):
            weight[i][j] = remote(tmp[j])

    w = kruskal(n, weight)
    if w == -1:
        print(-1)
    else:
        print(sum(map(sum, weight)) - w)
    
    
    
