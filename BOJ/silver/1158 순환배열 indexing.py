
# n, k = map(int, input().split())
#
# arr = [x for x in range(1, n+1)]
#
# idx = -1
#
# result = []
# while len(arr) != 1:
#     idx = idx + k
#     print(idx, result)
#     if idx >= len(arr):
#         idx = idx - len(arr)-1
#     else:
#         result.append(arr[idx])
#         arr.remove(arr[idx])
# print(result)

# 여기서 문제는 해당 값을 지워버리고, idx 위치가 해당 값을 가리켜버리면 안 된다.


# n, k = map(int, input().split())
#
# arr = [x for x in range(1, n+1)]
#
# table = dict() # 이미 결과에 담은 것 확인 용
#
# result = []
# idx = -1
# cnt = 0
# while len(arr) != 1:
#     if result == []:
#         idx += k
#         result.append(arr[idx])
#         table[arr[idx]] = 1
#         idx -= 1
#     else:
#         if cnt == k:
#             if arr[idx] not in table:
#                 result.append(arr[idx])
#                 table[arr[idx]] = 1
#                 cnt = 0
#                 idx -= 1
#             else:
#                 if idx >= len(arr):  idx = 0
#                 else:                idx += 1
#         else:
#             if arr[idx] in table:
#                 if idx >= len(arr):  idx = 0
#                 else:                idx += 1
#             else:
#                 if idx >= len(arr):  idx = 0
#                 else:                idx += 1
#                 cnt += 1
#         print(idx, cnt)
#         print(result)

# 이런식으로 접근해야 할 듯.

N, K = map(int, input().split())
arr = [i for i in range(1, N + 1)]  # 맨 처음에 원에 앉아있는 사람들

answer = []  # 제거된 사람들을 넣을 배열
num = 0  # 제거될 사람의 인덱스 번호

for t in range(N): # 제거될 사람의 갯수는 배열에 있는 모든 사람이므로, 1번만 순회해도 된다.
    num += K - 1
    if num >= len(arr):  # 배열 길이를 초과하는 index라면
        num = num % len(arr) # 나머지로 앞에 index로 옮김. 이게 이 코드의 핵심이다.

    answer.append(str(arr.pop(num)))
print("<", ", ".join(answer)[:], ">", sep='')

# 어떤 N, K값이 들어온다 하더라도 반드시 한 번에 한 개만 마주한다.