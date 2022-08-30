
# def solution(arr):
#     answer = []
#     for k in arr:
#         if k not in answer:
#             answer.append(k)
#     return answer
#
# 위 코드는 아예 set과 같은 결과를 내보낸다.


def solution(arr):
    answer = []
    answer.append(arr[0])
    cnt = 0

    for i in arr[1:]:
        if i == answer[cnt]:
            pass
        else:
            answer.append(i)
            cnt += 1
    return answer

## 다른 사람 코드 ##
def no_continuous(s):
    result = []
    for c in s:
        if (len(result) == 0) or (result[-1] != c):
            result.append(c)
    return result





def no_continuous(s):
    a = [ v for i,v in enumerate(s) if s[i-1] != s[i]]
    return a

