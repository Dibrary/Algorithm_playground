
'''
만일 A가 permutation이면 1을 반환, 아니라면 0을 반환

여기서 permutation의 의미는 순서대로.. 인가?
'''


def solution(A):
    A.sort()
    tmp = [x for x in range(1, len(A)+1)]
    if A == tmp:
        return 1
    else:
        return 0

# 위 코드 100%


print(solution([4,1,3,2]))
print(solution([4,1,3]))




