# import sys
# sys.setrecursionlimit(10**9)
#
# def fib1(n):
#     if n < 2:
#         return n
#     return fib1(n-1)+fib1(n-2)
#
# if __name__=="__main__":
#     print(fib1(16))


# 위 코드로 하면 이미 구한 경우에도 계속 구하는 '재귀'가 일어남.

# memo = {0:0, 1:1} # 사전을 이용하는 방법도 알아두자.
#
# def fib3(n):
#     if n not in memo: # 안에 없으면
#         memo[n] = fib3(n-1)+fib3(n-2) # 추가하는데, 재귀로 들어가서 구한 값을 추가한다.
#     return memo[n]
#
# if __name__=="__main__":
#     print(fib3(116))

# 파이썬은 모든 함수를 메모라이징 하는 decorator가 있다.

from functools import lru_cache

@lru_cache(maxsize=None) # maxsize란 가장 최근의 호출을 캐시할 수 있는 크기. None으로 하면 이 캐시에 제한을 없엔다.
def fib4(n):
    if n<2:
        return n
    return fib4(n-2) + fib4(n-1)

if __name__=="__main__":
    print(fib4(16))




def fib6(n):
    yield 0
    if n > 0 : yield 1
    last = 0
    next = 1
    for _ in range(1, n):
        last, next = next, last+next
        yield next

if __name__=="__main__":
    for i in fib6(20):
        print(i)

