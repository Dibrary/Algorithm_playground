
def printKthToLast(head, k):
    if head == None:
        return 0

    index = printKthToLast(head.next, k)+1
    if index == k:
        print(head.val, "this is value")
    return index

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


print(printKthToLast(a, 1))
print(printKthToLast(a, 2))
print(printKthToLast(a, 3))
print(printKthToLast(a, 4))



