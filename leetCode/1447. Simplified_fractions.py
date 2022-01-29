
n = 6

result = []
for i in range(1, n):
    for s in range(i+1, n+1):
        if i == 1:
            result.append("%d/%d"%(i,s))
        elif s%i != 0:
            result.append("%d/%d"%(i,s))
print(result)

# 기약분수는 다 제외해야 한다.

