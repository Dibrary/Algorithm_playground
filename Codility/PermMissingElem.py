
def solution(A):
    tmp = [x for x in range(1, len(A)+2)]

    for x in tmp:
        if x not in A:
            return x

# 위 코드는 60%점 받은 코드.




print(solution([2,3,1,5]))





