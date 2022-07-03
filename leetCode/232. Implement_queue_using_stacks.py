
'''
먼저 들어온게 먼저 나가게,
stack을 사용하자.
'''

class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop(0)

    def peek(self) -> int:
        return self.stack[0]

    def empty(self):
        return True if len(self.stack)==0 else False


## 다른 사람 코드 ##

class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output






class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # move everything to the first stack
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(x)

        while self.stack1:
            self.stack2.append(self.stack1.pop())
        print(self.stack2)

    def pop(self) -> int:
        return self.stack2.pop()

    def peek(self) -> int:
        return self.stack2[-1]

    def empty(self) -> bool:
        if self.stack1 or self.stack2:
            return False
        return True






class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        if len(self.pop_stack) == 0:
            while len(self.push_stack) > 0:
                val = self.push_stack.pop()
                self.pop_stack.append(val)

        return self.pop_stack.pop()

    def peek(self) -> int:
        if len(self.pop_stack) == 0:
            return self.push_stack[0]
        else:
            return self.pop_stack[-1]

    def empty(self) -> bool:
        if len(self.push_stack) == 0 and len(self.pop_stack) == 0:
            return True
        return False