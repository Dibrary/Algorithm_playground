
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


n, k = map(int, input().split())

arr = [x for x in range(1, n+1)]

table = dict() # 이미 결과에 담은 것 확인 용

result = []
idx = -1
cnt = 0
while len(arr) != 1:
    if result == []:
        idx += k
        result.append(arr[idx])
        table[arr[idx]] = 1
        idx -= 1
    else:
        if cnt == k:
            if arr[idx] not in table:
                result.append(arr[idx])
                table[arr[idx]] = 1
                cnt = 0
                idx -= 1
            else:
                if idx >= len(arr):  idx = 0
                else:                idx += 1
        else:
            if arr[idx] in table:
                if idx >= len(arr):  idx = 0
                else:                idx += 1
            else:
                if idx >= len(arr):  idx = 0
                else:                idx += 1
                cnt += 1
        print(idx, cnt)
        print(result)


# 이런식으로 접근해야 할 듯.



