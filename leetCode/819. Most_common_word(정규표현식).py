import re

# class Solution:
#     def mostCommonWord(self, paragraph, banned):
#         if len(paragraph.split(" ")) == 1:
#             if paragraph not in banned:
#                 noti = [",", ".", "!"]
#                 for s in noti:
#                     paragraph = paragraph.replace(s, "")
#                 return paragraph.lower()
#
#
#
#         table = dict()
#         noti = [",","."]
#         for s in noti:
#             paragraph = paragraph.replace(s, " ")
#
#         tmp = paragraph.split(" ") # 공백으로 잘라도 특수기호는 들어간다. (. , 등등) 특수 기호를 replace로 미리 처리.
#
#         for m in tmp:
#             m = m.lower()
#             if m not in banned and m != " " and m != "":
#                 if m not in table:
#                     table[m] = 1
#                 else:
#                     table[m] += 1
#
#         max_value = 0
#         result = None
#         for k in table:
#             if table[k] >= max_value:
#                 max_value = table[k]
#                 result = k
#         return result



# k = Solution()
# print(k.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
#
# print(k.mostCommonWord("a.",[])) # a가 나와야 됨.
# print(k.mostCommonWord("Bob!", ["hit"])) # bob이 나와야 됨
# print(k.mostCommonWord("Bob", [])) # bob이 나와야 됨.

# print(k.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"])) # b가 나와야 됨.

'''
위 방식으로 계속 여러 조건을 확인해 나가다 보면 끝이 없다.

그래서 '정규표현식'을 사용하는 것.

'''
import collections

class Solution:
    def mostCommonWord(self, paragraph, banned):

        noti = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]  # 이렇게 하는 방법도 있다.
        # 조건문으로 banned인 경우를 제외하고, [^\w]단어가 아닌 것은 ' ' 공백으로 sub(치환)한 후에, 소문자로 바꾸고 split한다.
        # split에 " " 이렇게 넣지 않으면 알아서 " "이든 "   "이든 관계없이 자른다

        # print(noti)
        counts = collections.Counter(noti)
        # print(counts) # Counter 객체다.
        # print(counts.most_common(1)) # 이렇게 하면 list안의 튜플 꼴로 가져온다.
        return counts.most_common(1)[0][0] # 그래서 [0][0]이 쓰이는 것.
k = Solution()

print(k.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"])) # b가 나와야 됨.

