
'''
중복된 문자를 제외하고 사전식 순서로 나타내라.

사전식 순서란 = 사전에서 가장 먼저 찾을 수 있는 문자열. 순서대로.


'''







### 책 풀이 ###
from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s):
        counter, seen, stack = Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] >0:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return ''.join(stack)



