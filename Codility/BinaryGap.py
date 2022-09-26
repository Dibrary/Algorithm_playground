
# def solution(N):
#     value = bin(N)[2:]
#     tmp = [x for x in value.split("1") if x != '']
#     if len(tmp) == 1 or tmp == []:
#         return 0
#     else:
#         return len(max(tmp))


# 위 코드는 26%밖에 못 받은 코드.

def solution(N):
    value = bin(N)[2:]
    index = []
    for idx, i in enumerate(value):
        if i == '1':
            index.append(idx)

    if index == [0]:
        return 0
    else:
        result = set()
        for x in range(len(index)-1):
            result.add(index[x+1] - index[x] -1)
        if result == {0}:
            return 0
        else:
            return max(result)

# 위 코드는 100% 받은 코드.


print(solution(1041))
print(solution(16))
print(solution(15))
print(solution(5))




