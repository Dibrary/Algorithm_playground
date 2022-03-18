
table = []

n = int(input())
for _ in range(n):
    tmp = list(input())
    tmp.sort()
    if tmp not in table:
        table.append(tmp)

print(len(table))


