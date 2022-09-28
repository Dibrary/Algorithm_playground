def solution(X, A):
    tmp = set()

    for idx, k in enumerate(A):
        if k == X:
            table = list(tmp)
            flag = True
            table.sort()
            for index, m in enumerate(table):
                if index != 0:
                    if m - table[index - 1] == 1:
                        continue
                    else:
                        flag = False
                        break
            if flag == True:
                return idx
        else:
            tmp.add(k)

# 위 코드는 예제만 통과한 코드다. 0%;;;;


print(solution(5, [1,3,1,4,2,3,5,4]))


