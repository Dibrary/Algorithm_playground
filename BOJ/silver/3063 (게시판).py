
'''
문제에서 구하고자 하는 것은 처음 붙인 것의 '보이는 넓이'다.
단순히 점의 갯수로 세기엔 문제가 있다.

'''

# from collections import defaultdict
#
# t = int(input())
#
# for _ in range(t):
#     x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split()) # 왼쪽아래, 오른쪽 위 이렇게 값이 주어진다.
#
#     first = set()
#     for x in range(x1, x2+1):
#         for y in range(y1, y2+1):
#             first.add((x, y))
#
#     second = set()
#     for x in range(x3, x4+1):
#         for y in range(y3, y4+1):
#             second.add((x, y))
#
#     points = first - first.intersection(second)
#
#     table = defaultdict(list)
#     for m in points:
#         table[m[0]].append(m[1])
#
#     result = 0
#     for k in table.keys():
#         result += len(table[k])-1
#     print(result)

# 위 코드는 에러 있다. 왜냐하면, 차집합에서 뺀 것이 곧 넓이를 의미하지 않음 =_=;;

# t = int(input())
#
# for _ in range(t):
#     x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split()) # 왼쪽아래, 오른쪽 위 이렇게 값이 주어진다.
#
#     first = set()
#     for x in range(x1, x2):
#         for y in range(y1, y2):
#             first.add((x, y, x+1 ,y+1)) # 점의 갯수를 세는게 아니라, 면적(왼쪽아래, 오른쪽 위 점)을 add함.
#
#     second = set()
#     for x in range(x3, x4):
#         for y in range(y3, y4):
#             second.add((x, y, x+1, y+1))
#
#     print(len(first- second))

# 위 코드는 12%에서 메모리 초과로 나옴.

t = int(input())

for _ in range(t):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split()) # 왼쪽아래, 오른쪽 위 이렇게 값이 주어진다.

    first = set()
    for x in range(x1, x2):
        for y in range(y1, y2):
            first.add((x, y, x+1 ,y+1)) # 점의 갯수를 세는게 아니라, 면적(왼쪽아래, 오른쪽 위 점)을 add함.

    for x in range(x3, x4):
        for y in range(y3, y4):
            if (x, y, x+1, y+1) in first:
                first.remove((x, y, x+1, y+1))

    print(len(first))

# 위 코드도 메모리초과로 나온다. 임시로 값을 1~10000 범주로 넣어보면, 실행에 시간이 매우 오래걸림.
















