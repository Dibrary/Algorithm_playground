
# n, m = map(int, input().split())  # 세로, 가로
#
# castle = []
# for _ in range(n):
#     castle.append(list(input()))
#
# castle_vertical = []
# for x in range(m):
#     tmp = []
#     for y in range(n):
#         tmp.append(castle[y][x])
#     castle_vertical.append(tmp)
#
# cnt = 0
# for y in range(n):
#     for x in range(m):
#         if set(castle[y]) == {'.'} and set(castle_vertical[x]) == {'.'}:
#             castle[y][x] = "X"
#             cnt += 1
# print(cnt)

# 2%에서 틀림

# n, m = map(int, input().split())  # 세로, 가로
#
# castle = []
# for _ in range(n):
#     castle.append(list(input()))
#
# castle_vertical = []
# for x in range(m):
#     tmp = []
#     for y in range(n):
#         tmp.append(castle[y][x])
#     castle_vertical.append(tmp)
#
# cnt = 0
# for y in range(n):
#     for x in range(m):
#         if set(castle[y]) == {'.'} and set(castle_vertical[x]) == {'.'}:
#             castle[y][x] = "X"
#             castle_vertical[y][x] = "X" # vertical 체크를 안 해줬었음.
#             cnt += 1
# print(cnt)

# 위 코드도 2%에서 틀림.

'''
핵심은 대각선으로 한 번만 가면서 확인하면 될듯?
'''















