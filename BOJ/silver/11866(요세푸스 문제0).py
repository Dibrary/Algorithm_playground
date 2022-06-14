
n, k = map(int, input().split())

# arr = [x for x in range(1, n+1)]
#
# idx = 0
# idx = k-1
# results = [arr[idx]]
# arr[idx] = 0
#
# no = 1
# while set(arr) != {0}: # 여기서 일일이 확인 해야 되서 문제;;
#     idx += 1
#     if idx >= len(arr):
#         idx = 0
#     if arr[idx] != 0:
#         if no == k:
#             results.append(arr[idx])
#             arr[idx] = 0
#             no = 1
#         else:
#             no += 1
#
# print(f"<{', '.join(map(str, results))}>")

# 위 코드는 에제는 통과하지만 시간초과 걸림.

n, k = map(int, input().split())



