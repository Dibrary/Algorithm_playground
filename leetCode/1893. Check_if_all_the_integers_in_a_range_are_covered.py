
def isCovered(ranges, left, right):
    table = set()
    for i in ranges:
        for k in range(i[0], i[1] + 1):
            table.add(k)

    table = list(table)
    tmp = [ x for x in range(left, right+1) ]

    for i in tmp:
        if i not in table:
            return False
        else:
            continue
    return True

print(isCovered([[1,2],[3,4],[5,6]],2,5))
print(isCovered([[1,10],[10,20]],21,21))

# 통과