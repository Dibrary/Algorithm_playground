
# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     values = []
#     for _ in range(n):
#         values.append(list(map(int, input().split())))
#
#     first = 0
#     values.sort(key=lambda x:(x[0], x[1])) # 첫 번째 값으로 오름차순
#     print(values)
#     first_min_value = values[0]
#     for i in range(1, len(values)):
#         if first_min_value[0] < values[i][0]:
#             first += 1
#
#     second = 0
#     values.sort(key=lambda x:(x[1], x[0])) # 두 번째 값으로 오름차순
#     print(values)
#     second_min_value = values[0]
#     for j in range(1, len(values)):
#         if second_min_value[1] < values[j][1]:
#             second += 1
#     print(first, second)

'''
뭘 기준으로 잡느냐가 관건 같은데...
첫 번째 예제에서 5 5를 기준으로 잡아버리면 나머지 죄다 탈락.

주어지는 숫자가 '점수'가 아니라, '순위'다. 이거 주의!
'''

t = int(input())

for _ in range(t):
    n = int(input())

    persons = []

    std = None
    cnt = 0

    for _ in range(n):
        a, b = map(int, input().split())
        persons.append((a, b))
    persons.sort(key=lambda x: (x[0], x[1]))
    std = list(persons[0]) # 숫자 갱신을 위해 list로 변경해서 넣어둠
    cnt += 1

    for i in persons[1:]:
        if i[1] < std[1]:
            std[1] = i[1] # 계속 낮은 숫자일 때만 갱신
            cnt += 1
    print(cnt)







## 다른 사람 코드 ##

import sys

T = int(input())  # 테스트케이스

for i in range(0, T):
    Cnt = 1
    people = []

    N = int(input())
    for i in range(N):
        Paper, Interview = map(int, sys.stdin.readline().split())
        people.append([Paper, Interview])

    people.sort()  # 서류 기준 오름차순 정렬
    Max = people[0][1]

    for i in range(1, N):
        if Max > people[i][1]:
            Cnt += 1
            Max = people[i][1]

    print(Cnt)







import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    rank = [list(map(int, input().split())) for _ in range(N)]
    rank_asc = sorted(rank)
    top = 0
    result = 1

    for i in range(1, len(rank_asc)):
        if rank_asc[i][1] < rank_asc[top][1]:
            top = i
            result += 1

    print(result)