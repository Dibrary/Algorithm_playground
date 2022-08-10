

def find(node):

    low_value = 10e9
    while low_value != node:
        if nodes[node] <= low_value:
            low_value = nodes[node]
            node = nodes[node]


def union(a, b):
    if b != a:
        nodes[b] = a
        find(b)

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






