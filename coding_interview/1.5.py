
def oneEditInsert(s1, s2):
    print("insert")
    index1 = 0
    index2 = 0

    while index2 < len(s2) and index1 < len(s1):
        print(index2, index1)
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True


def oneEditReplace(s1, s2):
    print("replace")
    foundDifference = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if foundDifference:
                return False
            foundDifference = True
    return True

def oneEditAway(first, second):
    if len(first) == len(second):
        return oneEditReplace(first, second)
    elif len(first) + 1 == len(second):
        return oneEditInsert(first, second)
    elif len(first) - 1 == len(second):
        return oneEditInsert(second, first)
    return False


print(oneEditAway('pale', 'bale'))