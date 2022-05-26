
# 큰 것을 먼저 놓고 배치.
def solution(s):
    tmp = list(s)
    tmp.sort(reverse=True)
    return "".join(map(str,tmp))


# 다른사람 코드
def solution(s):
    return ''.join(sorted(s, reverse=True)) # 곧바로 문자열에서도 사용할 수 있다.
