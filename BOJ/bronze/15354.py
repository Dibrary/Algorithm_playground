
# n = int(input())
#
# tmp = set()
# for _ in range(n):
#     tmp.add(input())
#
# print(len(tmp)+1)

# 틀림 set으로 하면 안 된다.

n = int(input())

tmp = []
for i in range(n):
    if i == 0:
        tmp.append(input())
    else:
        value = input()
        if value == tmp[-1]:
            continue
        else:
            tmp.append(value)
print(len(tmp)+1)



