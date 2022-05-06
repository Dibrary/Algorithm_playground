
table = [1]
for i in range(2, 400):
    table.append(table[-1]+i)

n = int(input())

index = 0
value = 0

for idx, k in enumerate(table):
    if n <= k:
        index = idx
        value = k
        break

cnt = table[index] - n
print(cnt, index, value)

upper = 1 + cnt
under = (index + 1) - cnt

print("%d/%d"%(upper, under))

# 지그재그로 이동할 때 x, y축에 해당되는 값 에서만 이상하게 나옴.





