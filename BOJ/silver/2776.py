#
# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     m = int(input())
#     values = list(map(int, input().split()))
#     for i in values:
#         if i in arr:
#             print(1)
#         else:
#             print(0)

# 위 처럼 코드 작성하면 시간오버됨.




# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split())) # 비교 대상이 되는 것을 정렬 해 두고
#     arr.sort()
#
#     m = int(input())
#     values = list(map(int, input().split()))
#     for i in values:
#         start = 0
#         end = len(arr)-1
#
#         flag = 0
#
#         while start <= end: # 2진 탐색을 적용한다.
#             mid = (start + end)//2
#             if i > arr[mid]:      start = mid + 1
#             elif i < arr[mid]:    end = mid - 1
#             elif i == arr[mid]:
#                 print(1)
#                 flag = 1
#                 break
#         if flag == 0:
#             print(0)

# 홀 2진탐색도 시간초과 나온다.

from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr_dict = defaultdict(int) # 이렇게 하면 default 값이 0으로 자동생성된다.
    for i in arr:
        if i not in arr_dict:
            arr_dict[i] = 1
        else:
            continue

    m = int(input())
    values = list(map(int, input().split()))
    for j in values:
        print(arr_dict[j]) # 값이 있으면 1로 출력되고, 없으면 default로 0이 출력됨.




