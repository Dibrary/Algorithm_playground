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





def test(firstList, secondList):
    if firstList == [] or secondList == []: return []

    lower = min(min(min(firstList, secondList)))
    upper = max(max(max(firstList, secondList)))

    first_result, second_result = set(),set()
    for i in range(lower, upper+1):
        for k in firstList:
            if k[0]<= i <= k[1]:
                first_result.add(i)
        for l in secondList:
            if l[0]<= i <= l[1]:
                second_result.add(i)
    result = list(first_result&second_result)
    # 리스트로 어떻게 다시 묶느냐가 관건.
