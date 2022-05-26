# n = int(input())
#
# for _ in range(n):
#     m = int(input())
#
#     values = list(map(int, input().split()))
#     values += list(map(int, input().split()))
#
#     values.sort()
#
#     cnt = 0
#
#     for i in values:
#         tmp = [i, i+500, i+1000, i+1500]
#
#         flag = 0
#         for k in tmp:
#             if k in values:
#                 values[values.index(k)] = 0 # 여기서 미리 지워버리는 문제인듯?
#             else:
#                 flag = 1
#         if flag == 1:
#             continue
#         else:
#             cnt += 1
#     print(cnt-1)

# 50% 까지 진행되고 틀림.


# n = int(input())
#
# for _ in range(n):
#     m = int(input())
#
#     values = list(map(int, input().split()))
#     values += list(map(int, input().split()))
#
#     values.sort()
#
#     cnt = 0
#
#     for i in values:
#         tmp = [i, i+500, i+1000, i+1500]
#
#         flag = 0
#         for k in tmp:
#             if k not in values:
#                 flag = 1
#         if flag == 1:
#             continue
#         else:
#             for j in tmp:
#                 values[values.index(j)] = 0
#             cnt += 1
#             print(values)
#     print(cnt-1)

# 50% 까지 진행되고 틀림.

# 왼쪽과 오른쪽을 나눠 관리해야 함;

n = int(input())

for _ in range(n):
    m = int(input())

    left_values = list(map(int, input().split()))
    right_values = list(map(int, input().split())) # 항상 정렬된 채로 들옴

    cnt = 0

    for i in left_values:
        tmp = [i, i+500, i+1000, i+1500]

        flag = 0
        for idx, k in enumerate(tmp):
            if idx < 2: # 앞의 2개는 왼쪽 기록
                if k not in left_values:
                    flag = 1
            else: # 뒤의 2개는 오른쪽 기록
                if k not in right_values:
                    flag = 1
        if flag == 1:
            continue
        else:
            for idx, s in enumerate(tmp):
                if idx < 2:
                    left_values[left_values.index(s)] = 0
                else:
                    right_values[right_values.index(s)] = 0
            cnt += 1
    print(cnt)

