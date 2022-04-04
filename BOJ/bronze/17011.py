
n = int(input())

for _ in range(n):

    string = input()
    table = dict()
    keys = []
    for i in string:
        if i in table:
            table[i] += 1
        else:
            table[i] = 1
        if i not in keys:
            keys.append(i)

    result = ""
    for s in keys:
        result += str(table[s]) + " " + str(s) +" "

    print(result[:-1])

# 이렇게 코딩하면 중간에 똑같이 나오는 것이 한 곳에서만 처리됨;



