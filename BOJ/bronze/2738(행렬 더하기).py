# n, m = list(map(int, input().split()))
# arr1, arr2 = [0 for _ in range(n)], [0 for _ in range(m)]
#
# for i in range(n):
#     arr1[i] = (list(map(int, input().split())))
# for j in range(m):
#     arr2[j] = (list(map(int, input().split())))
#
# for i in range(0, len(arr1)):
#     for j in range(0, len(arr1[0])):
#         arr1[i][j] = arr1[i][j] + arr2[i][j]
#
# for k in arr1:
#     tmp = ""
#     for i in k:
#         tmp += str(i) + " "
#     print("%s" % (tmp[:-1]))

# EOFError 남.



n, m = map(int, input().split())

arr_a = []
for _ in range(n):
    arr_a.append(list(map(int, input().split())))

arr_b = []
for _ in range(n):
    arr_b.append(list(map(int, input().split())))

result = [[] for _ in range(m)]

for y in range(n):
    for x in range(m):
        result[y].append(arr_a[y][x]+arr_b[y][x])

for k in result:
    print(" ".join(map(str, k)))

# 위 코드 index Error 남; 예제는 잘 돌아감.


### 다른 사람 코드 ###

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
    tmp = list(map(int, input().split()))

    for j in range(m):
        board[i][j] += tmp[j] # 2번째 for문에서 아예 한 번에 덧셈을 처리해버린다.

for x in board:
    print(" ".join(map(str, x)))