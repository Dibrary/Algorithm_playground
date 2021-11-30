'''
스택 기능하는 객체 구현하기
'''

from collections import deque

class MinStack:
    def __init__(self):
        self.stack = deque()

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def top(self):
        value = self.pop()
        self.push(value)
        return value

    def getMin(self):
        return min(self.stack)

if __name__=="__main__":
    tmp = MinStack()
    tmp.push(-2)
    tmp.push(0)
    tmp.push(-3)
    print(tmp.getMin())
    print(tmp.pop())
    print(tmp.top())
    print(tmp.getMin())