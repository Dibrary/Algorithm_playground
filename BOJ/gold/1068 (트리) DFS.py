
# 문제 보자마자 딱 맞닥뜨린 어려움은 입력으로 트리구성을 어떻게 하느냐.
# 리프노드는 left, right가 모두 None인 노드

'''
리프노드를 탐색하는 알고리즘을 수행할 때나 제거하는 노드가 나왔을 때 탐색을 종료하게 하면?


예제 입력에서
9
-1 0 0 2 2 4 4 6 6
4

이 의미는,
0이 root이고,
1과 2는 o을 부모로 두고 있고,
3과 4는 2를 부모로 두고 있고,
5와 6은 4를 부모로 두고 있고,
7과 8은 6을 부모로 두고 있다는 의미다.

여기서 4를 제거한다는 입력을 준 것.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right=  right
#
# n = int(input())
# arr = list(map(int, input().split()))
# target = int(input()) # 삭제 해야 하는 node
# if target == 0:
#     print(0)
# else:
#     table = dict()
#
#     root = TreeNode(arr[0])
#     table[0] = root
#     for i in range(1, n):
#         table[i] = TreeNode(i)
#         if i%2 != 0:
#             table[arr[i]].left = table[i]
#         elif i%2 == 0:
#             table[arr[i]].right = table[i]
#
#     cnt = 0
#
#     table[target] = None
#     if target%2 != 0:
#         table[arr[target]].left = None
#     elif target%2 == 0:
#         table[arr[target]].right = None
#
#     queue = [table[0]]
#     while queue:
#         node = queue.pop(0)
#         if node.left == None and node.right == None:
#             cnt += 1
#         else:
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#
#     print(cnt)

# 입력 중간에 -1이 생겨버리면 KeyError가 발생한다.
# 이진트리라는 말이 없다. 이진트리가 아닐 수도.

# class TreeNode:
#     def __init__(self, val=0):
#         self.val = val
#         self.childs = []
#
#
# n = int(input())
# arr = list(map(int, input().split()))
# target = int(input())  # 삭제 해야 하는 node
#
# if target == 0:
#     print(0)
# else:
#     table = dict()
#
#     root = TreeNode(arr[0])
#     table[0] = root
#
#     for i in range(1, n):
#         table[i] = TreeNode(i)
#
#         if i % 2 != 0 and arr[i] != -1:
#             table[arr[i]].left = table[i]
#         elif i % 2 == 0 and arr[i] != -1:
#             table[arr[i]].right = table[i]
#         elif arr[i] == -1:
#             table[0].childs.append(table[i])

# 근데 부모가 없다면 -1인 것이다. -1이면 무조건 root로 있는 것이 아니라.


# n = int(input())
# arr = list(map(int, input().split()))
# x = int(input())
# if x == 0:
#     print(0)
# else:
#     leaf = [0 for x in range(len(arr))]
#
#     for k in range(1, len(arr)):
#         if k == x or arr[arr[k]] == 10e9: # 오른쪽 조건 추가하면 x 해당되는 것 이후부터 모조리 10e9로 바뀜.
#             arr[k] = 10e9
#         if k not in arr:
#             leaf[k] = 1
#
#     # print(leaf) # 이렇게 하면 leaf인 경우만 들어온다.
#     cnt = 0
#     for a, b in zip(arr, leaf):
#         if a != -1 and a != 10e9 and b == 1:
#             cnt += 1
#     print(cnt)

# 위 코드는 예제는 다 통과하지만, 틀렸다.

'''
입력 받는 배열 데이터로 트리 데이터를 어떻게 구현할까?
'''


# arr = [[1,2],[],[3,4],[],[5,6],[],[7,8]] # 이 꼴일 때 아래 dfs 함수 적용됨.
# n = int(input())
# arr = [[] for _ in range(n)]
# tmp = list(map(int, input().split()))
#
# for k in range(len(tmp)):
#     for i in range(len(tmp)):
#         if k == tmp[i]:
#             arr[k].append(i)
# x = int(input())
#
# visited = [False] * len(arr)
# cnt = 0
#
# def dfs(start):
#     global cnt
#
#     visited[start] = True
#     if arr[start] == []:
#         cnt += 1
#     if start != x:
#         for k in arr[start]:
#             if visited[k] == False:
#                 dfs(k)
#     else:
#         return
#
# dfs(0)
# print(cnt)







n = int(input())
arr = [[] for _ in range(n)]
tmp = list(map(int, input().split()))

for k in range(len(tmp)):
    for i in range(len(tmp)):
        if k == tmp[i]:
            arr[k].append(i)
x = int(input())
if x == 0:
    print(0)
else:
    visited = [False] * len(arr)
    cnt = 0

    def dfs(start):
        global cnt

        visited[start] = True
        for k in arr[start]:
            if visited[k] == False and k != x:
                if arr[k] == []:
                    cnt += 1
                dfs(k)

    dfs(0)
    print(cnt)

# 위 코드도 틀림.




## 다른 사람 코드 ##
import sys
input = sys.stdin.readline

def dfs(num, arr):
    arr[num] = -2 # num(삭제해야 할 노드 번호)인덱스의 배열 값을 삭제함.

    for i in range(len(arr)):
        if num == arr[i]: # 삭제 노드와 같은 숫자인 경우
            dfs(i, arr) # 더 깊게 들어간다. (들어가면 당연히 -2로 값이 바뀔 것)

n = int(input())
arr = list(map(int, input().split()))
k = int(input()) # 삭제해야 할 노드 번호
count = 0

dfs(k, arr)

count = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr: # -2도 아니고, 다른 노드의 부모도 아닌 경우(해당 배열에 값이 있으면, 다른 노드의 부모다.)
        count += 1 # 갯수 센다.
print(count)







import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
nl = list(map(int,input().rstrip().split()))
dn = int(input().rstrip())

tree=[[] for _ in range(n)]
for i in range(len(nl)):
    if nl[i] != -1:
        tree[nl[i]].append(i)
if nl[dn] != -1:
    del tree[nl[dn]][tree[nl[dn]].index(dn)]

def cntleaf(R):
    global lcnt
    visited[R] = 1
    if not tree[R]:
        lcnt += 1
    else:
        for i in tree[R]:
            if not visited[i]:
                cntleaf(i)
    return lcnt

tcnt = 0
for i in range(len(nl)):
    visited = [0]*(n)
    if nl[i] == -1 and i != dn:
        lcnt = 0
        tcnt += cntleaf(i)
print(tcnt)







def DFS(num, l):
    l[num] = -2
    for i in range(len(l)):
        if num == l[i]:
            DFS(i, l)

n = int(input())
l = list(map(int, input().split()))
k = int(input())
cnt = 0

DFS(k, l)
cnt = 0
for i in range(len(l)):
    if l[i] != -2 and i not in l:
        cnt += 1
print(cnt)







N = int(input())
node = list(map(int, input().split()))
A = int(input())

stack = [A]
node[A] = -2

while stack:
    a = stack.pop()
    for i in range(node.count(a)):
        stack.append(node.index(a))
        node[stack[-1]] = -2
res = 0

for i in range(N):
    if node[i] != -2 and node[i] != -1 and node.count(i) == 0:
        res += 1

if len(node) == 2:
    print(1)
    quit()

print(res)


