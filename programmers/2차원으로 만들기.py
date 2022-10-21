
def solution(num_list, n):
    result = []
    tmp = []

    for x in num_list:
        tmp.append(x)
        if len(tmp) == n:
            result.append(tmp)
            tmp = []
    return result


print(solution([1,2,3,4,5,6,7,8],2))
print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948],3))


## 다른 사람 코드 ##

import numpy as np
def solution(num_list, n):
    li = np.array(num_list).reshape(-1,n)
    return li.tolist()






def solution(num_list, n):
    answer = []

    for i in range(len(num_list)//n) :
        answer.append(num_list[i*n:(i+1)*n])

    return answer
