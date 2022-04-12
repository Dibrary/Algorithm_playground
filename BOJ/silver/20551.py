
# def binary_search(value):
#     start_idx = 0
#     end_idx = len(arr)
#
#     while start_idx <= end_idx: # 이진탐색
#         mid = int((start_idx+end_idx)/2)
#         if arr[mid] < value:
#             start_idx = mid+1
#         elif arr[mid] > value:
#             end_idx = mid-1
#         elif arr[mid] == value:
#             return mid
#
#
# a, n = map(int, input().split())
#
# table = dict()
# arr = []
# for i in range(a):
#     value = int(input())
#     arr.append(value)
#     if value not in table:
#         table[value] = 1
#
# arr.sort()
#     # if i == 0:
#     #     arr.append(value)
#     # else:
#     #     if arr[0] >= value:
#     #         arr.insert(0,value)
#     #     elif arr[-1] < value:
#     #         arr.append(value)
#     # 이 코드는 중간에 양 끝 값 사이 value가 들어오면 처리 못함.
#
# for _ in range(n):
#     find_value = int(input())
#     if find_value not in table: # 굳이 dict를 따로 만들 필요 없이 None이 나오면 안에 없다는 것.
#         print("-1")
#     else:
#         print(binary_search(find_value))

# 위 코드 시간초과


def binary_search(value):
    start_idx = 0
    end_idx = len(arr)

    while start_idx <= end_idx: # 이진탐색
        mid = int((start_idx+end_idx)/2)
        if mid >= len(arr):
            break
        if arr[mid] < value:
            start_idx = mid+1
        elif arr[mid] > value:
            end_idx = mid-1
        elif arr[mid] == value:
            return mid

a, n = map(int, input().split())

arr = []
for i in range(a):
    value = int(input())
    arr.append(value)

arr.sort()

for _ in range(n):
    find_value = int(input())
    result = binary_search(find_value)
    if result == None:
        print("-1")
    else:
        print(result)

# 위 코드도 틀림