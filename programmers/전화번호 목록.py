
'''
이 코드에서 궁금한 점.
1. 길이가 다른 경우 확인을 어떻게 해야 하는가.
2. 왜 이 문제가 hash(dict)를 써야 할까?

'''

phone_book = ["119", "97674223", "1195524421"]

# def solution(phone_book):
#     phone_book.sort(key=lambda x: len(x)) # 정렬 후에 짧은 것 부터 갖다 댄다.
#
#     for i in range(len(phone_book) - 1):
#         for j in range(i + 1, len(phone_book)):
#             if phone_book[i] == phone_book[j][:len(phone_book[i])]:
#                 return False
#     return True
#
# print(solution(phone_book))

# 위 코드는 정확성 테스트는 모두 통과. 효율성 테스트에서 2개 시간초과 걸림.

# def solution(phone_book):
#     phone_book.sort(key=lambda x: len(x))
#
#     table = dict()
#     length = list(set(len(m) for m in phone_book))
#
#     for i in length:
#         if i not in table:
#             table[i] = []
#             for k in range(len(phone_book)):
#                 table[i].append(phone_book[k][:i])
#
#     for x in phone_book:
#         if x in table[len(x)]:
#             return False
#     return True
# 위 코드는 dict를 써보려고 했던건데, 자기 자신이 포함된 경우가 있어서 안 됨.

# def solution(phone_book):
#     phone_book.sort(key=lambda x: len(x)) # 정렬 후에 짧은 것 부터 갖다 댄다.
#
#     for i in range(len(phone_book) - 1):
#         for j in range(i + 1, len(phone_book)):
#             if phone_book[i] in phone_book[j][:len(phone_book[i])]: # 문자열은 비교를 in으로도 할 수 있다.
#                 return False
#     return True
# 효율성 테스트에서 2개 시간초과 걸림.

from collections import defaultdict

def solution(phone_book):
    phone_book.sort(key=lambda x: len(x)) # 정렬 후에 짧은 것 부터 갖다 댄다.

    tmp = defaultdict(list)
    for x in phone_book:
        idx = phone_book.index(x)
        tmp[x] = [k[:len(x)] for k in phone_book[:idx] + phone_book[idx+1:]] # 여기서 이미 2중 for문이라 결국 같은 코드다.
        if x in tmp[x]:
            return False
    return True

# 위 방법도 시간초과 걸린다.
def solution(phone_book): # 이 코드가 가장 깔끔.
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]): # 다음거보다 작은 경우에만.
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                return False
    return True







## 다른 사람 코드 ##
def solution(phone_book):
    answer = True
    phone_book.sort() # sort가 길이별 정렬이 아니다.!!!

    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]): # 다음거보다 작은 경우에만.
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer










def solution(phone_book):
    # 1. Hash map을 만든다
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    print(hash_map)
    # 2. 접두어가 Hash map에 존재하는지 찾는다
    for phone_number in phone_book:
        jubdoo = ""
        for number in phone_number:
            jubdoo += number
            # 3. 접두어를 찾아야 한다 (기존 번호와 같은 경우 제외)
            if jubdoo in hash_map and jubdoo != phone_number:
                return False
    return True










def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True