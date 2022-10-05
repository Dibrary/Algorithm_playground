
def solution(my_string, n):
    result = ""
    for k in my_string:
        result += k*n
    return result


## 다른 사람 코드 ##
def solution(my_string, n):
    return ''.join(i*n for i in my_string) # 한 번에 처리가 가능하다





