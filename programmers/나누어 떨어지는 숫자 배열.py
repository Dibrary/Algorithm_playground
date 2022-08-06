
def solution(arr, divisor):
    answer = [x for x in arr if x%divisor == 0]
    answer.sort()
    return answer if answer != [] else [-1]


## 다른 사람 코드 ##

def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]


def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0]
    arr.sort()
    return arr if len(arr) != 0 else [-1]
