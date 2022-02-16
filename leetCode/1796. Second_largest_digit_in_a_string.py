
def secondHighest(s):
    table = set()
    for i in s:
        if i.isdigit():
            table.add(i)
    if len(table) <= 1:
        return -1
    table = list(table)
    table.sort()
    return table[-2]



print(secondHighest("dfa12321afd"))
print(secondHighest("abc1111"))