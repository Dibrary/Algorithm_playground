firstList = [[0,2],[5,10],[13,23],[24,25]]
values = []
for i in firstList:
    for k in range(i[0], i[1]+1):
        values.append(k)
print(values)

secondList = [[1,5],[8,12],[15,24],[25,26]]
result = []
for j in secondList:
    for s in range(j[0], j[1]+1):
        if s in values:
            result.append(s)
print(result)