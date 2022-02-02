class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def nextLargerNodes(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next

    result = []
    tmp = values[0]
    start_idx = 0

    for k in range(1, len(values)):
        if values[k] > tmp:
            for j in range(start_idx, k):
                result.append(values[k])
            result.append(0)
            if k < len(values)-1:
                tmp = values[k+1]
                start_idx = k+1
    return result

e = ListNode(5)
d = ListNode(3,e)
c = ListNode(4,d)
b = ListNode(7,c)
a = ListNode(2,b)

print(nextLargerNodes(a))

# 위 코드 [1,7,5,1,9,2,5,1] 하면 7,0,9,9,0,5,0 나오는데, 답은 7,9,9,9,0,5,0,0 이어야 한다.






