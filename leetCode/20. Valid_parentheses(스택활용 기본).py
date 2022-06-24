
'''
스택으로 넣고
끝나는 괄호가 나올 때 마다 스택 맨 위랑 비교.
'''


class Solution:
    def isValid(self, s: str) -> bool:
        tb = {")": "(",
              "}": "{",
              "]": "["}

        s = list(s)
        stack = []

        for sb in s:
            if sb not in tb:
                stack.append(sb)
            else:
                temp = stack.pop() if stack else ''
                if tb[sb] != temp:
                    return False

        return len(stack) == 0


### 다른 사람 코드 ###
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        syntax = {")": "(", "}": "{", "]": "["}

        for i in s:
            if i in syntax:
                top_stack = stack.pop() if stack else '$'
                if (top_stack != syntax[i]):
                    return False
            else:
                stack.append(i)

        return not stack







class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {']': '[', '}': '{', ')': '('}
        for c in s:
            if c not in matching:
                stack.append(c)
            elif len(stack) == 0 or stack.pop() != matching[c]:
                return False
        return len(stack) == 0