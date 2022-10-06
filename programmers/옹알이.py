
'''
문자를 따라가면서 pass, fail을 체크할 수도 있는데,
가능한 경우의 수가 몇 개 안 되어서 dict로 미리 만들어놓고 비교해보기로 함.

'''

from itertools import permutations

def make_table():
    table = dict()

    for k in range(1, 5):
        for x in permutations(["aya", "ye", "woo", "ma"],k):
            value = "".join(map(str, x))
            if value not in table:
                table[value] = 1

            value = "".join(map(str, x[::-1]))
            if value not in table:
                table[value] = 1
    return table

def solution(babbling):
    table = make_table()
    cnt = 0
    for x in babbling:
        if x in table:
            cnt += 1
    return cnt

# 위 코드 1개 틀림 87.5점

def solution(babbling):
    cnt = 0
    for s in babbling:
        s = s.replace("aya", "")
        s = s.replace("ye", "")
        s = s.replace("woo", "")
        s = s.replace("ma", "")
        if s == "":
            cnt += 1
    return cnt

# 위 방법은 예제 2번에서 실패. 같은 발음이 연속되면 안 된다.




