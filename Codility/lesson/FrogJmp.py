
# def solution(X, Y, D):
#     cnt = 0
#     while X+D < Y:
#         X = X+D
#         cnt += 1
#     return cnt+1

# 위 코드는 33% 정답 코드.;;

def solution(X, Y, D):
    if (Y-X)%D == 0:
        return (Y-X)//D
    else:
        return (Y-X)//D+1

# 위 코드는 100% 코드

print(solution(10,85,30))



