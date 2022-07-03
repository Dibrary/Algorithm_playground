
'''
큐 사용해서 스택 구현하기

'''

class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def empty(self):
        return True if len(self.stack) == 0 else False


### 다른 사람 코드 ###

class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.insert(0, x)

    def pop(self) -> int:
        return self.queue.pop(0)

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        if not self.queue:
            return True
        return False







class MyStack:

    def __init__(self):
        self._queue1 = []
        self._queue2 = []

    def push(self, x: int) -> None:
        self._queue1.append(x)

    def pop(self) -> int:
        while len(self._queue1) != 1:
            self._queue2.append(self._queue1.pop(0))
        result = self._queue1.pop()
        self._queue1, self._queue2 = self._queue2, self._queue1
        return result

    def top(self) -> int:
        return self._queue1[-1]

    def empty(self) -> bool:
        return len(self._queue1) == 0





class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.t = x

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.t = self.q1.pop(0)
            self.q2.append(self.t)
        result = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1
        return result

    def top(self) -> int:
        return self.t

    def empty(self) -> bool:
        return True if not self.q1 and not self.q2 else False