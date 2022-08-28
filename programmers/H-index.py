
'''
예제에서 4로 잡지 못하는 이유는 4 이상인 논문이 4개 이상이 아니기 때문.
'''


# def solution(citations):
#     citations.sort()
#     return citations[len(citations)//2]

# 이렇게 간단히 생각했더니 이건 아예 틀림

def solution(citations):
    citations.sort()

    max_value = citations[-1]
    min_value = citations[0]
    maximum_value = 0

    for x in range(min_value, max_value):
        lower = len([m for m in citations if m <= x]) # x번 이하 인용되었다면, x번까지 포함.
        higher = len([m for m in citations if m >= x]) # x번 이상 인용되었다면, x번까지 포함.
        if lower <= x and higher >= x:
            if maximum_value <= x:
                maximum_value = x

    return maximum_value

# 위 코드는 딱 1개 실패함.

def solution(citations):
    citations.sort()
    # citations.sort(reverse=True) # 이렇게 하는 것이 시간이 더 짧게 걸린다.
    maximum_value = 0

    for x in range(0, 1001): # 여기를 아예 조건에 주어진 갯수만 하게 끔 수정 해 봄.
        lower = len([m for m in citations if m <= x]) # x번 이하 인용되었다면, x번까지 포함.
        higher = len([m for m in citations if m >= x]) # x번 이상 인용되었다면, x번까지 포함.
        if lower <= x and higher >= x:
            if maximum_value <= x:
                maximum_value = x

    return maximum_value

# 통과


## 다른 사람 코드 ##
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0











def solution(citations):
    h = []
    answer = 0

    for cit in citations:
        h.append(citations.index(cit)+1)

    citations.sort(reverse=True)

    for i in range(len(citations)):
        if h[i] == citations[i]:
            answer = h[i]
        if h[i] > citations[i]:
            answer = h[i] - 1
            break
        elif h[i] < citations[i]:
            answer = h[i]
    return answer