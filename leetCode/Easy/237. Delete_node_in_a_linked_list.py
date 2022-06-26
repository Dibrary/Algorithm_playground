
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteNode(node):

    result_root = head

    while head:
        if head.next.val == node:
            head.next = head.next.next
        else:
            head = head.next

# 이 문제는 list가 전달인자에 없다 =_=;;

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

# =_= 그냥 이게 답이란다...