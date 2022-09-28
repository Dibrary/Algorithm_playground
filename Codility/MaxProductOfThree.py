
# def solution(A):
#     A.sort()
#     return A[-1]*A[-2]*A[-3]
# 위 코드는 44% 받음
# 근데 위 코드는 음수가 있으면 최대값이 안 된다? 음수도 큰 값이 오른쪽에 위치하게 된다.

def solution(A):
    plus_cnt = 0
    minus_cnt = 0
    zero_cnt = 0

    for x in A:
        if x > 0:
            plus_cnt += 1
        elif x < 0:
            minus_cnt += 1
        else:
            zero_cnt += 1
    A.sort()

    if plus_cnt >= 3:
        return A[-1]*A[-2]*A[-3]
    elif (plus_cnt == 2 or plus_cnt == 1)and minus_cnt >= 2:
        return A[0]*A[1]*A[-1]
    elif plus_cnt == 0 and minus_cnt >= 3:
        return A[-1] * A[-2] * A[-3]

# 위 코드는 55% 받음.



print(solution([-3,-2,1,2,5,6]))
print(solution([-1,-2,-3,-4,-5]))
print(solution([5, 1,-4,-2,-5,-6]))
