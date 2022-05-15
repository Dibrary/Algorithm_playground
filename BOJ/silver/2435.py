# n, k = map(int, input().split())
# tmp = list(map(int, input().split()))
#
# result = 0
# for i in range(n - k + 1):
#     if sum(tmp[i:i + k]) >= result:
#         result = sum(tmp[i:i + k])
#
# print(result)

# 위 코드 24% 정도에서 틀림

n, k = map(int, input().split())
tmp = list(map(int, input().split()))

result = set()
for i in range(n - k + 1):
    result.add(sum(tmp[i:i + k]))

print(max(result))

# set으로 바꾸니까 통과 됨.


