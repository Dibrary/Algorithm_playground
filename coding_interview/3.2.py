
class Stack:
    def __init__(self):
        self.min = int(10e9)
        self.stack = []

    def push(self, value):
        if value <= self.min:
            self.min = value
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def min_v(self): # 한 번 만에 min값 꺼내는 메서드
        return self.min


OBJ = Stack()
OBJ.push(11)
OBJ.push(34)
OBJ.push(2)
OBJ.push(14)

print(OBJ.min_v())

print(OBJ.pop())
print(OBJ.pop())
print(OBJ.pop())
print(OBJ.pop())