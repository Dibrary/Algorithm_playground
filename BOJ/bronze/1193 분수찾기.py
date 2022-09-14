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


arr = [x for x in range(4500)]
total_cnt = [0, 1, 3] + [0 for x in range(4500)]
for k in range(3, len(arr)):
    total_cnt[k] = total_cnt[k-1]+arr[k]

n = int(input())
if n == 1:
    print(f"{1}/{1}")
idx = 0
for k in range(len(total_cnt)):
    if n <= total_cnt[k]:
        idx = k
        break

print(idx, "idx")
total = total_cnt[idx-1]

if idx%2 == 0:
    upper = 1
    under = idx
    total += 1

    if total == n:
        print(f"{upper}/{under}")
    else:
        for x in range(idx-1):
            upper += 1
            under -= 1
            total += 1
            if total == n:
                print(f"{upper}/{under}")
else:
    upper = idx
    under = 1
    total += 1
    if total == n:
        print(f"{upper}/{under}")
    else:
        for x in range(idx-1):
            upper -= 1
            under += 1
            total += 1
            if total == n:
                print(f"{upper}/{under}")

# 100%까지 가놓고 틀렸다고 나옴 =_="??






## 다른 사람 코드 ##


