
def solution(numbers, direction):
    if direction == 'left':
        return numbers[1:]+numbers[:1]
    else:
        return numbers[-1:]+numbers[:-1]




## 다른 사람 코드 ##

from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)








from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    numbers.rotate(1 if direction == 'right' else -1)
    return list(numbers)