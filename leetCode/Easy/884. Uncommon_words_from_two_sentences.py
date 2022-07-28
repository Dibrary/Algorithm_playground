
def uncommon(s1, s2):
    table = dict()
    for i in s1.split():
        if i not in table:
            table[i] = 1
        else:
            table[i] += 1

    for i in s2.split():
        if i not in table:
            table[i] = 1
        else:
            table[i] += 1

    result = []
    for i in table:
        if table[i] == 1:
            result.append(i)
    return result

print(uncommon("this apple is sweet", "this apple is sour"))

