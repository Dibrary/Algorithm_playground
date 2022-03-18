#
# table = {" ":0}
#
# for idx, s in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 1):
#     table[s] = idx
#
# n = int(input())
# values = list(map(int, input().split()))
# string = input()
#
# flag = 0
# for k in string:
#     if table[k] in values:
#         values.remove(table[k])
#     else:
#         flag = 1
#         break
#
# if flag == 0 and values == []:
#     print("y")
# else:
#     print("n")

# 위 코드는 46%에서 시간초과 걸림.

table = {" ":0}

for idx, s in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 1):
    table[s] = idx

n = int(input())
values = list(map(int, input().split()))
values_table = dict()

for s in values:
    if s not in values_table:
        values_table[s] = 1
    else:
        values_table[s] += 1

# 이 부분을 dict로 바꾸니까 시간초과 없어짐

string = input()

flag = 0
for k in string:
    if table[k] in values_table:
        values_table[table[k]] -= 1
    else:
        flag = 1
        break

if flag == 0 and max(values_table.values()) == 0:
    print("y")
else:
    print("n")