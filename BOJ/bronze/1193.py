#
# table = [1]
# for i in range(2, 400):
#     table.append(table[-1]+i)
#
# n = int(input())
#
# index = 0
# value = 0
#
# for idx, k in enumerate(table):
#     if n <= k:
#         index = idx
#         value = k
#         break
#
# cnt = n-table[index-1]-1
#
# if index%2 == 0:
#     upper = index+1
#     under = 1
#     for k in range(cnt):
#         upper -= 1
#         under += 1
# else:
#     upper = 1
#     under = index + 1
#     for k in range(cnt-1, -1, -1):
#         upper += 1
#         under -= 1
#
# print("%d/%d"%(upper, under))

# 지그재그로 이동할 때 x, y축에 해당되는 값 에서만 이상하게 나옴.

# 위 코드 틀림

table = [1]
for i in range(2, 400):
    table.append(table[-1]+i)

n = int(input())

index = 0
value = 0

for idx, k in enumerate(table):
    if n <= k:
        index = idx
        value = k
        break

cnt = n-table[index-1]-1

if index%2 == 0:
    upper = index+1
    under = 1
    for k in range(cnt):
        upper -= 1
        under += 1
else:
    upper = 1
    under = index + 1
    for k in range(cnt-1, -1, -1):
        upper += 1
        under -= 1

print("%d/%d"%(upper, under))






