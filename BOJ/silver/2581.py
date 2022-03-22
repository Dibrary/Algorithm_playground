# import math
#
# sheve = [x for x in range(10010)]
# sheve[1] = 0
#
# for s in sheve[2:]:
#     for k in range(2, int(math.sqrt(10010))):
#         if s * k < len(sheve):
#             sheve[s * k] = 0
#
# m = int(input())
# n = int(input())
#
# total = sum(sheve[m: n + 1])
# if total == 0:
#     print(-1)
# else:
#     print(total)
#     tmp = list(set(sheve[m: n + 1]))
#     tmp.sort()
#     print(tmp[1])


# 인덱스 에러 남
# m과 n이 인덱스가 아니다. 그냥 해당 값의 범주에 들어가는 모든 값을 확인해야 됨.

import math

sheve = [x for x in range(10010)]
sheve[1] = 0

for s in sheve[2:]:
    for k in range(2, int(math.sqrt(10010))):
        if s * k < len(sheve):
            sheve[s * k] = 0

m = int(input())
n = int(input())

sheve_set = list(set(sheve))
values = []
for k in sheve_set:
    if m <= k <= n:
        values.append(k)
if values == []:
    print(-1)
else:
    values.sort()
    print(sum(values))
    print(values[0])