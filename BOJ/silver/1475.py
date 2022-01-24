table = [0]*11

n = input()
for i in n:
    table[int(i)] += 1

midvalue = (table[6]+table[9])//2 # 이 부분이 문제였다.

table[9] = 0
table[6] = 0
print(table, midvalue)
if max(table) > midvalue:
    print("%d"%(max(table)))
else:
    print("%d"%(midvalue))

# 위의 것은 에러가 남.

table = [0]*11

n = input()
for i in n:
    table[int(i)] += 1

if (table[6]+table[9])%2 == 0:
    midvalue = (table[6]+table[9])//2
else:
    midvalue = ((table[6]+table[9])//2)+1
table[9] = 0
table[6] = 0
if max(table) > midvalue:
    print("%d"%(max(table)))
else:
    print("%d"%(midvalue))