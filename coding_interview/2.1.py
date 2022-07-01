
class List:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next


f = List(6)
e = List(5, f)
d = List(2, e)
c = List(3, d)
b = List(2, c)
a = List(1, b)

def removeDuplicate(head):
    tmp = set()
    prev = None
    result = head

    while head:
        value = head.val

        if value in tmp: # 있으면 이렇게 중복 제거,
            prev.next = head.next # 그 전 노드와 그 이후 노드를 연결.
            head = prev.next      # 이후 노드를 head로 재설정.
        else:
            tmp.add(value)
            prev = head
            head = head.next

    return result


result = removeDuplicate(a)

while result:
    print(result.val)
    result = result.next





