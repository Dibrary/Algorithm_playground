
# from itertools import permutations
#
# def solution(n, k):
#     for idx, x in enumerate(permutations([m for m in range(1, n+1)],3)):
#         if idx == (k-1):
#             return list(x)

# 예제는 통과하는데 전부 실패함 ;;
# 아 변수로 넣어야 할 부분에 3을 넣어버림.

from itertools import permutations

def solution(n, k):
    for idx, x in enumerate(permutations([m for m in range(1, n+1)],n)): # 여기 n 부분.
        if idx == (k-1):
            return list(x)

# 위 방법으로는 정확성 테스트 전부 통과하지만, 효율성에서 시간초과로 다 실패됨.
# 백트래킹을 써야 할 거 같은데...












## 다른 사람 코드 ##





