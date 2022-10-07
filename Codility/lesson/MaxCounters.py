
'''
예제만 보고 파악한 것은
1. 전체 길이보다 큰 값이 나오면 현재 있는 값 중 최대 값으로 모든 값이 초기화가 된다.
2. 각 값이 길이보다 작은 숫자값이면 해당 index 위치에 값이 +1 된다.
'''


def solution(N, A):
    temp = [0 for _ in range(N+1)]
    for x in range(1, len(A)+1):
        if A[x-1] <= N:
            temp[A[x-1]] += 1
        else:
            max_value = max(temp)
            temp = [max_value for _ in range(N+1)]
    return temp[1:]

# 위 코드는 66% 받은 코드다. 굉장히 큰 경우에 대해서 timeout 3개가 걸림.



print(solution(5, [3,4,4,6,1,4,4]))





