
left = 1; right = 22

table = [x for x in range(0, right+1)]

for i in range(2, 23):
    for k in range(2, 23):
        tmp = i*k
        if tmp > len(table):
            continue
        else:
            table[tmp] = 0
print(table)
