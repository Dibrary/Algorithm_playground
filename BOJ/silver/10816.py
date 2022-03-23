
n = int(input())
table = dict()
for k in map(int, input().split()):
    if k not in table:
        table[k] = 1
    else:
        table[k] += 1

m = int(input())
values = list(map(int, input().split()))

result = ""
for s in values:
    if s in table: result += str(table[s])+" "
    else:          result += "0 "

print(result[:-1])