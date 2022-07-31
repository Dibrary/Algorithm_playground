
# 헷갈리는 점은 문자가 같은 문자열이 여럿일 경우 사전순을 어떻게 처리할 것인가가 문제.

def solution(strings, n):
    table = dict()
    words = []

    for i in strings:
        if i[n] not in words:
            words.append(i[n])
        if i[n] not in table:
            table[i[n]] = [i]
        else:
            table[i[n]].append(i)

    words.sort()

    result = []
    for i in words:
        value = sorted(table[i])
        result += value
    return result

# print(solution(["sun","bed","car"],1))

print(solution(["abce", "abcd", "cdx"],2))

### 다른사람 코드 ###

def strange_sort(strings, n):
    return sorted(strings, key=lambda x: x[n]) # n번째 글자로 정렬해서 반환.

### 다른 사람 코드 ###
def strange_sort(strings, n):
    def sortkey(x):
        return x[n]
    strings.sort(key=sortkey)
    return strings

