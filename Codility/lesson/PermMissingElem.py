
'''
순서대로 있는 값 중에 '하나' 없는 그 값을 찾는 문제.
'''

# def solution(A):
#     tmp = [x for x in range(1, len(A)+2)]
#
#     for x in tmp:
#         if x not in A:
#             return x

# 위 코드는 60%점 받은 코드.


def solution(A):
    adding = sum(A)
    total = sum([x for x in range(1, len(A)+2)])
    return total - adding

# 100% 통과. 시간복잡도는 O(N) or O(N * log(N))라고 한다.


print(solution([2,3,1,5]))





