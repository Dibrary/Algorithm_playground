
# def solution(before, after):
#     for x in before:
#         if x in after:
#             after = after.replace(x,"") # replace를 쓰면 여러 개 있어도 한 번에 다 바뀌어 버린다.
#             print(after)
#     return 1 if after == "" else 0
#
# print(solution("olleh", "hello"))
# print(solution("allpe", "apple")) # 얜 왜 1 나오지



from collections import defaultdict

def solution(before, after):
    before_dict = defaultdict(int)
    after_dict = defaultdict(int)
    for b, a in zip(before, after):
        before_dict[b] += 1
        after_dict[a] += 1

    if before_dict == after_dict:
        return 1
    else:
        return 0

print(solution("olleh", "hello"))
print(solution("allpe", "apple")) 

## 다른 사람 코드 ##
def solution(before, after):
    before = sorted(before) # 정렬로 곧바로 비교
    after = sorted(after)
    if before == after:
        return 1
    else:
        return 0


