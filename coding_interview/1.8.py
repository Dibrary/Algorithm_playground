

def func(tmp):
    y = 0
    x = 0
    for k in range(len(tmp)):
        for j in range(len(tmp[0])):
            if tmp[k][j] == 0:
                y = k
                x = j

    for k in range(len(tmp)):
        for j in range(len(tmp[0])):
            if k == y:
                tmp[k][j] = 0
            if j == x:
                tmp[k][j] = 0
    return tmp

tmp = [[1,2,3,4,5],[4,0,6,7,4],[7,8,5,4,9],[7,5,9,4,2],[1,5,3,4,8]]
print(func(tmp))

