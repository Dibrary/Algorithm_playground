
'''
문제를 보자마자 세그먼트 트리를 하면 빠르겠다는 생각이 들지만,
세그먼트 트리를 어떻게 구현하는지를 모름.
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

for _ in range(m):
    a, b = map(int, input().split())
    print(min(arr[a-1:b]))

# 위 코드는 30%에서 시간초과된다.


## 다른 사람 코드 ##

from math import *
import sys

def init(node, start, end):
    if start == end:
        tree_min[node] = arr[start]
        return tree_min[node]

    mid = (start + end)//2
    tree_min[node] = min(init(node*2, start, mid), init(node*2 + 1, mid + 1, end))
    return tree_min[node]

def query(node, start, end, left, right):
    if start > right or end < left:
        return 1000000001
    if left <= start and end <= right:
        return tree_min[node]
    mid = (start + end)//2
    return min(query(node*2, start, mid, left, right), query(node*2 + 1, mid + 1, end, left, right))

# main
n, m = [int(x) for x in sys.stdin.readline().split()]

h = int(ceil(log2(n))) # 트리 높이
t_size = 1 << (h+1) # 트리 총 노드 수

arr = []
tree_min = [0] * t_size  # 최솟값 저장

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

init(1, 0, n-1)

for _ in range(m):
    a, b = [int(x) for x in sys.stdin.readline().split()]
    print(query(1, 0, n-1, a-1, b-1)) # a와 b는 index가 아니라 번째 수.









from math import *
import sys

def initMin(node, start, end):
    if start == end:
        tree_min[node] = arr[start]
        return tree_min[node]

    mid = (start + end) // 2
    tree_min[node] = min(initMin(node*2, start, mid), initMin(node*2+1, mid+1, end))
    return tree_min[node]

def initMax(node, start, end):
    if start == end:
        tree_max[node] = arr[start]
        return tree_max[node]

    mid = (start + end) // 2
    tree_max[node] = max(initMax(node * 2, start, mid), initMax(node * 2 + 1, mid + 1, end))
    return tree_max[node]

def queryMin(node, start, end, left, right):
    if start > right or end < left:
        return sys.maxsize

    if left <= start and end <= right:
        return tree_min[node]

    mid = (start + end) // 2
    return min(queryMin(node * 2, start, mid, left, right),
               queryMin(node*2 + 1, mid + 1, end, left, right))

def queryMax(node, start, end, left, right):
    if start > right or end < left:
        return 0

    if left <= start and right >= end:
        return tree_max[node]

    mid = (start + end) // 2
    return max(queryMax(node * 2, start, mid, left, right),
               queryMax(node * 2 + 1, mid + 1, end, left, right))

# main
n, m = [int(x) for x in sys.stdin.readline().split()]

h = int(ceil(log2(n)))
t_size = 1 << (h + 1)

arr = []
tree_min = [0] * t_size
tree_max = [0] * t_size

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

initMin(1, 0, n - 1)
initMax(1, 0, n - 1)

for _ in range(m):
    a, b = [int(x) for x in sys.stdin.readline().split()]

    print(queryMin(1, 0, n - 1, a - 1, b - 1))









import sys

n_number, n_query = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(n_number)]


def forward_update(tree, nthnode, value):
    while nthnode <= n_number:
        tree[nthnode] = min(tree[nthnode], value)
        nthnode += nthnode & -nthnode


def backward_update(tree, nthnode, value):
    while nthnode:
        tree[nthnode] = min(tree[nthnode], value)
        nthnode -= nthnode & -nthnode


def query(forward_tree, backward_tree, start, end):
    result = 1000000000

    cur = end - (end & -end)
    prev = end

    while cur >= start:
        result = min(result, forward_tree[prev])
        prev = cur
        cur -= cur & -cur

    cur = start + (start & -start)
    prev = start

    while cur <= end:
        result = min(result, backward_tree[prev])
        prev = cur
        cur += cur & -cur

    return min(result, nums[prev - 1])


if __name__ == '__main__':
    forward_tree = [1000000000] * (n_number + 1)
    backward_tree = [1000000000] * (n_number + 1)

    for seq, number in enumerate(nums):
        forward_update(forward_tree, seq + 1, number)
        backward_update(backward_tree, seq + 1, number)

    for _ in range(n_query):
        start, end = map(int, sys.stdin.readline().split())
        print(query(forward_tree, backward_tree, start, end))


