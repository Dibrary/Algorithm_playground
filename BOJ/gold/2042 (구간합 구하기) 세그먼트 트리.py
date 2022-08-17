
'''
세그먼트 트리는 구간합, 최대/ 최소 구하기로 나눌 수 있고,
세그먼트 트리 index = 주어진 질의 index + 2^k - 1 이다.

리프 노드 갯수가 데이터 갯수 이상이 되게 트리 배열을 만든다.
트리 배열 크기는 2^k >= N을 만족하는 k의 최소값을 구한 후, (2^k)*2 를 트리 배열 크기로 정의하면 된다.

오른쪽 끝에부터 채워넣은 후에, 각 리프의 합, 최소값, 최대값을 부모 노드위치에 쓴다. (찾고자 하는 목적 값에 따라 다르게 연산하면 됨)


중간에 수의 변경이 빈번하게 일어나면 변경에도 시간이 비교적 적게 걸리는 세그먼트 트리를 쓰자.
'''


n, m, k = map(int, input().split()) # n은 수 갯수, m은 수 변경 횟수, k는 구간합 구하는 횟수.
arr = []
for _ in range(n):
    arr.append(int(input()))


for _ in range(k):
    a, b, c = map(int, input().split())
    if a == 1: # 값 교체 (b번째 수를 c로 변경)

        pass # 갱신이 이뤄질 때 마다 arr을 새롭게 해 줘야 한다. (세그먼트 트리로 하면 새롭게 바뀌는 부분과 연관 있는 곳만 손대면 된다.)

    elif a == 2: # 구간합 구해서 출력 (b번째 수부터 c번째 수 까지의 합)
        pass







## 다른 사람 코드 ##

import sys

input = sys.stdin.readline


# 세그먼트 트리 생성
# node가 담당하는 구간 [start, end]

def init(node, start, end):
    # node가 leaf 노드인 경우 배열의 원소 값을 반환.
    # node가 리프 노드인 경우, 리프 노드는 배열의 그 원소를 가져야 하기 때문에 tree[node] = a[start]가 됩니다.
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        # 재귀함수를 이용하여 왼쪽 자식과 오른쪽 자식 트리를 만들고 합을 저장.
        tree[node] = init(node * 2, start, (start + end) // 2) + init(node * 2 + 1, (start + end) // 2 + 1, end)
        return tree[node]


# 구간 합 구하기
# node가 담당하는 구간 [start, end]
# 합을 구해야하는 구간 [left, right]
def subSum(node, start, end, left, right):
    # 겹치지 않기 때문에, 더 이상 탐색을 이어갈 필요가 없다.
    if left > end or right < start:
        return 0

    # 구해야하는 합의 범위는 [left, right]인데, [start, end]는 그 범위에 모두 포함되고
    # 그 node의 자식도 모두 포함되기 때문에 더 이상 호출을 하는 것은 비효율적이다.
    if left <= start and end <= right:
        return tree[node]

    # 왼쪽 자식과 오른쪽 자식을 루트로 하는 트리에서 다시 탐색을 시작해야한다.
    # node 의 왼쪽 자식은 node*2, 오른쪽 자식은 node*2+1이 됩니다.
    # 또, node가 담당하는 구간이 [start,end] 라면 왼쪽 자식은 [start,(start+end)/2], 오른쪽 자식은 [(start+end)/2+1,end]를 담당
    return subSum(node * 2, start, (start + end) // 2, left, right) + subSum(node * 2 + 1, (start + end) // 2 + 1, end, left, right)


def update(node, start, end, index, diff):
    if index < start or index > end:
        return

    tree[node] += diff

    # 리프 노드가 아닌 경우에는 자식도 변경해줘야 하기 때문에 검사해야함.
    if start != end:
        update(node * 2, start, (start + end) // 2, index, diff)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)


n, m, k = map(int, input().rstrip().split())

l = []
tree = [0] * 3000000

for _ in range(n):
    l.append(int(input().rstrip()))

init(1, 0, n - 1)

for _ in range(m + k):
    a, b, c = map(int, input().rstrip().split())

    if a == 1:
        b = b - 1
        diff = c - l[b]
        l[b] = c
        update(1, 0, n - 1, b, diff)
    elif a == 2:
        print(subSum(1, 0, n - 1, b - 1, c - 1))

