
import sys
input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#     arr = []
#     n = int(input())
#     for _ in range(n):
#         arr.append(input().strip())
#     arr.sort(key=lambda x: (len(x),x)) # 길이, 값으로 정렬 (값정렬은 필요 없어보이는듯)
#
#     flag = 0
#     for s in range(0, len(arr)-1):
#         tmp = arr[s]
#         length = len(tmp)
#         for k in range(s+1, len(arr)):
#             if flag == 1:
#                 break
#             else:
#                 if tmp == arr[k][:length]:
#                     flag = 1
#                     break
#                 else:
#                     continue
#     if flag == 1:
#         print("NO")
#     else:
#         print("YES")
# 위 방법은 전부 확인하는 것으로, 시간초과 난다.

t = int(input())
for _ in range(t):

    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(input())  # 문자열로 받아야 길이별 정렬이 가능.

    arr.sort()
    flag = 0
    for x in range(len(arr) - 1):
        if arr[x] == arr[x + 1][:len(arr[x])]:
            flag = 1
            break
    if flag == 1:
        print("NO")
    else:
        print("YES")








## 다른 사람 코드 ##











