
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    a_values, b_values = [],[]
    while headA:
        a_values.append(headA.val)
        headA = headA.next

    while headB:
        b_values.append(headB.val)
        headB = headB.next

    a_values = a_values[::-1]
    b_values = b_values[::-1]

    for i in range(0, max(len(a_values), len(b_values))):
        if a_values[i] != b_values[i]:
            return a_values[i]


e = ListNode(5)
d = ListNode(4)
c = ListNode(8)
b = ListNode(1)
a = ListNode(4)

d.next = e
c.next = d
b.next = c
a.next = b

ff = ListNode(5)
ee = ListNode(4)
dd = ListNode(8)
cc = ListNode(1)
bb = ListNode(6)
aa = ListNode(5)

ee.next = ff
dd.next = ee
cc.next = dd
bb.next = cc
aa.next = bb

print(getIntersectionNode(a, aa))
