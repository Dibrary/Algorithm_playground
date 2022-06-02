
# arr = []
#
# for i in range(5):
#     arr.append(list(map(int, input().split())))

# 무조건 세 줄만 완성되어도 빙고다.
# 숫자는 1부터 25까지 이므로 0을 지운 flag로 사용해도 된다.

# for k in range(len(arr)):
#     tmp = []
#     for j in range(len(arr[0])):
#         tmp.append(arr[k][j])
#     print(tmp) # 가로로 확인 법
# print("----")
#
# for k in range(len(arr)):
#     tmp = []
#     for j in range(len(arr[0])):
#         tmp.append(arr[j][k])
#     print(tmp) # 세로로 확인 법
# print("==-==")
# tmp = []
# for k in range(len(arr)):
#     for j in range(len(arr[0])):
#         if k == j:
#             tmp.append(arr[k][j])
# print(tmp)
#
# print("==-==")

# tmp = []
# for k in range(len(arr)+1):
#     for j in range(len(arr[0])):
#         if (k + j) == len(arr):
#             tmp.append(arr[j][-k])
# 이 코드는 위 코드와 같다.

# tmp=[]
# for k in range(len(arr)):
#     tmp.append(arr[k][len(arr)-1-k])
#
# print(tmp)

# 연습은 끝.

arr = []
for i in range(5):
    arr.append(list(map(int, input().split())))

def func(value):
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == value:
                arr[i][j] = 0 # 해당 값 0으로 변경

    for k in range(len(arr)):
        tmp = []
        for j in range(len(arr[0])):
            tmp.append(arr[k][j])
        tmp = set(tmp)
        if tmp == {0}:
            cnt += 1

    for k in range(len(arr)):
        tmp = []
        for j in range(len(arr[0])):
            tmp.append(arr[j][k])
        tmp = set(tmp)
        if tmp == {0}:
            cnt += 1

    tmp = []
    for k in range(len(arr)):
        for j in range(len(arr[0])):
            if k == j:
                tmp.append(arr[k][j])
    tmp = set(tmp)
    if tmp == {0}:
        cnt += 1

    tmp = []
    for k in range(len(arr)):
        tmp.append(arr[k][len(arr)-1-k])
    tmp = set(tmp)
    if tmp == {0}:
        cnt += 1

    if cnt == 3:
        return True
    else:
        return False

values = []
for _ in range(5):
    values.append(list(map(int, input().split())))


def loop_func(value):
    for k in value:
        if func(k):
            return k

for i in values:
    m = loop_func(i)
    if m != None:
        print(m)
        break

# 결과가 좀 이상하게 나옴.
