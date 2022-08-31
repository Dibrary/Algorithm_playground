
# import sys
# input = sys.stdin.readline
#
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

# 시간초과



# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     numbers = []
#     for _ in range(n):
#         numbers.append(input())
#
#     numbers.sort()
#     flag = "YES"
#     for i in range(len(numbers) - 1):
#         if len(numbers[i]) < len(numbers[i+1]):
#             if numbers[i+1][:len(numbers[i])] == numbers[i]:
#                 flag = "NO"
#                 break
#     print(flag)

# 25%에서 틀림.










