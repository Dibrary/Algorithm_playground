import sys

tmp = dict()

aaa = list(sys.stdin.readline() for _ in range(50))
for i in aaa:
    for k in i:
        if k not in tmp and k != " " and k != "\n":tmp[k] = 1
        elif k in tmp and k != " " and k != "\n":  tmp[k] += 1

max_count = 0
for j in "abcdefghijklmnopqrstuvwxyz":
    if j in tmp:
        if tmp[j] >= max_count:
            max_count = tmp[j]

result = ""
for j in "abcdefghijklmnopqrstuvwxyz":
    if j in tmp:
        if tmp[j] == max_count:
            result += j
print(result)
