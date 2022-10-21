
def solution(array, n):
    value = 10e6
    result = 0
    for x in array:
        if abs(n-x) < value:
            value = abs(n-x)
            result = x
        elif abs(n-x) == value:
            if x < result:
                result = x

    return result

print(solution([10,11,12],13))
# 위 코드는 1개 틀림 (같은 경우에 대한 처리가 없는 듯)




## 다른 사람 코드 ##
solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]





def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer




def solution(array, n):
    arr = {i:abs(n-i) for i in array}
    return sorted(arr.items(),key=lambda x: [x[1],x[0]])[0][0]





def solution(array, n):
    dict = {}
    for i in array:
        dict[i] = abs(n-i)
    dict = sorted(dict.items(), key = lambda x : (x[1],x[0]))

    return dict[0][0]