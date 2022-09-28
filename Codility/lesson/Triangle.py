
'''
3개를 뽑아다가 삼각형 구성이 가능하면 1을 반환,
단 하나도 만들지 못하면 0을 반환.
'''

# def solution(A):
#     for a in range(len(A)-2):
#         for b in range(a+1, len(A)-1):
#             for c in range(b+1, len(A)): # 문제는 이렇게 해버리면 효율성이 꽝이다.
#                 if a < b+c and b < a+c and c < a+b:
#                     return 1
#     return 0

def solution(A):
    table = dict()
    for k in A:
        table[k] = 1

    for a in range(len(A)-2):
        for b in range(a+1, len(A)-1):
            tmp = a+b
            for k in table.keys(): # 결국 위 코드랑 똑같은거 아닌가?
                if k < tmp and a < k+b and b < a+k:
                    return 1
    return 0

# 이 코드는 0% 받았다;;


print(solution([10,2,5,1,8,20]))

