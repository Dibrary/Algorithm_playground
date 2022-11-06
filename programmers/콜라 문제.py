
def solution(a, b, n):
    single_value = 0

    result = 0

    while n >= a:
        if n%a == 0:
            result += n//a
            n = n//a
        else:
            single_value = 1
            n = (n/a) - 1 # 여기가 문제다. 소수점으로 떨어질 경우 처리 어떻게 해야 할까.
            






