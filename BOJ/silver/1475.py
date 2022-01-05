table = [0]*11

n = input()
for i in n:
    table[int(i)] += 1

midvalue = (table[6]+table[9])//2
table[9] = 0
table[6] = 0
print(table, midvalue)
if max(table) > midvalue:
    print("%d"%(max(table)))
else:
    print("%d"%(midvalue))