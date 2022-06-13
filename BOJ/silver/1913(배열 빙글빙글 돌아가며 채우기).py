#
# n = int(input()) # 배열 가로, 세로 길이 값
# value = int(input()) # 찾고자 하는 값
#
# arr = [[0 for _ in range(n)] for _ in range(n)]
#
# arr[len(arr)//2][len(arr)//2] = 1 # 정 중앙에 1 넣음.
# start_value = 2

# for i in range(1, 4):
#     print(i)
#     if i%2 != 0:
#         for k in range(i):
#             arr[(len(arr)//2)-i][len(arr)//2] = start_value
#             start_value += 1
#         for m in range(i):
#             arr[len(arr) // 2-i][(len(arr) // 2)+i] = start_value
#             start_value += 1
#     else:
#         for k in range(i):
#             arr[(len(arr)//2)+i][len(arr)//2] = start_value
#             start_value += 1
#         for m in range(i):
#             arr[len(arr) // 2+i][(len(arr) // 2)-i] = start_value
#             start_value += 1
# print(arr)

# 위 코드는 1, 2, 3만 잘 채워짐..;;

n = int(input()) # 배열 가로, 세로 길이 값
value = int(input()) # 찾고자 하는 값

arr = [[0 for _ in range(n)] for _ in range(n)]

nx = len(arr)//2
ny = len(arr)//2
arr[ny][nx] = 1 # 정 중앙에 1 넣음.

start_value = 2


for k in range(1, n):
    if k%2 != 0:
        for m in range(k):
            ny -= 1
            arr[ny][nx] = start_value
            start_value += 1
        for s in range(k):
            nx += 1
            arr[ny][nx] = start_value
            start_value += 1
    else:
        for m in range(k):
            ny += 1
            arr[ny][nx] = start_value
            start_value += 1
        for s in range(k):
            nx -= 1
            arr[ny][nx] = start_value
            start_value += 1

# 위 코드까지만 하면 맨 왼쪽 값이 빈다.
for k in range(ny):
    ny -= 1
    arr[ny][nx] = start_value
    start_value += 1

# 위치 구하는 부분

y_idx = 0
x_idx = 0

for idx, k in enumerate(arr):
    if value in k:
        y_idx = idx
        x_idx = k.index(value)

for v in arr:
    print(" ".join(map(str, v)))

print(y_idx + 1, x_idx + 1)

'''
처음에 7x7 배열로 해보려 했더니 너무 복잡해서 3x3으로 기본 index를 잡고 난 이후 for문 범주를 확장시켰다.
'''

# 다른 사람 코드



