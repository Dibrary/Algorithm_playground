
table = [x for x in range(0, 1001)]

for k in range(2,1000):
    for i in range(2, 300):
        print(k, i)
        if k*i < len(table):
            if table[k*i] != 0:
                table[k*i] = 0
        elif k*i >= len(table):
            break
print(table)

