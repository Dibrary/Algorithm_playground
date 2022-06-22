
'''
1. 로그 가장 앞은 식별자.
2. 문자로 구성된 로그가 숫자 앞에 온다.
3. 식별자는 순서에 영향 X, 문자가 동일하면 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.

문제는 식별자 뒤에 몇 개가 올지 모름. (그떄그때 다름.)
'''


# class Solution:
#     def reorderLogFiles(self, logs):
#         words = []
#         digits = [] # 숫자 로그는 입력 순서대로.
#         for k in logs:
#             if k[:3] == "dig": # 먼저 나눠 담음. # 식별자가 반드시 dig라는 보장은 없다.
#                 digits.append(k)
#             else:
#                 words.append(k)
#
#         '''
#         여기서 문자 처리를 해야 한다.
#         '''
#         words.sort(key=lambda x:(x.split()[1:], x.split()[0])) # [1:] 이렇게 하면 갯수가 달라도 상관 없다.
#         return words+digits


class Solution:
    def reorderLogFiles(self, logs):
        words = []
        digits = [] # 숫자 로그는 입력 순서대로.
        for k in logs:
            if k.split(" ")[1].isdigit():  # 식별자가 반드시 dig라는 보장은 없다.
                digits.append(k)
            else:
                words.append(k)

        '''
        여기서 문자 처리를 해야 한다.
        즉, 핵심 코드는 바로 아래 줄.
        '''
        words.sort(key=lambda x:(x.split()[1:], x.split()[0])) # [1:] 이렇게 하면 갯수가 달라도 상관 없다.

        return words+digits

k = Solution()
k.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])


