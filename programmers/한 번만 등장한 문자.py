from collections import defaultdict
def solution(s):
    table = defaultdict(int)

    for x in s:
        table[x] += 1

    result = []
    for k in table.keys():
        if table[k] == 1:
            result.append(k)
    result.sort()
    return "".join(map(str, result))



## 다른 사람 코드 ##

def solution(s):
    answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
    return answer




def solution(s):
    answer = ''
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if s.count(c) == 1:
            answer += c
    return answer