
def largeGroupPositions(s):
    tmp = dict()
    for i in s:
        if i not in tmp:
            tmp[i] = 1
        else:
            tmp[i] += 1

    max_value=None
    max_count = 0
    for i in tmp:
        if tmp[i] >= max_count:
            max_value = i
            max_count = tmp[i]

    print(max_value, max_count)


largeGroupPositions("abbxxxxzzy")



# 문제 이해를 못함;;