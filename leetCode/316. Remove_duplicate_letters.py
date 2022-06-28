
'''
중복된 문자를 제외하고 사전식 순서로 나타내라.

사전식 순서란 = 사전에서 가장 먼저 찾을 수 있는 문자열. 순서대로.

'''

class Solution:
    def removeDuplicateLeters(self, s):
        tmp = list(s)
        tmp.sort()
        smallest = tmp[0] # 가장 사전순으로 빠른 문자.

        result = [smallest]
        s.index(smallest) # 여러 개 글자 있는 경우 index는 가장 맨 앞의 숫자를 반환한다.

        for i in range(s.index(smallest)-1,-1,-1): # 가장 사전순으로 앞에 와야 할 문자 중에 왼쪽에 있는 값 확인
            if s.count(s[i]) == 1:
                result.insert(0, s[i])

        for k in range(s.index(smallest)+1, len(s)): # 그 뒤에 오른쪽에 있는 값들 확인 후 담기
            if s[k] not in result:
                result.append(s[k])
        return ''.join(map(str, result))


k = Solution()
# print(k.removeDuplicateLeters("bcabc"))
# print(k.removeDuplicateLeters("ebcabc"))
# print(k.removeDuplicateLeters("ebcabce"))
# print(k.removeDuplicateLeters("cbacdcbc")) # 위 examples는 모두 통과

print(k.removeDuplicateLeters("leetcode")) # 반례가 생긴다...







### 책 풀이 ###
# from collections import Counter
#
# class Solution:
#     def removeDuplicateLetters(self, s):
#         counter, seen, stack = Counter(s), set(), [] # 스택을 이용한 풀이
#
#         for char in s:
#             counter[char] -= 1
#             if char in seen:
#                 continue
#             while stack and char < stack[-1] and counter[stack[-1]] >0:
#                 seen.remove(stack.pop())
#
#             stack.append(char)
#             seen.add(char)
#
#         return ''.join(stack)

class Solution:
    def removeDuplicateLetters(self, s): # 재귀를 사용한 풀이
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''
    
    

