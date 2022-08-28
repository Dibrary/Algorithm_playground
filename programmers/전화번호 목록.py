
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






