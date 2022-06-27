
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        tmp[left - 1:right] = tmp[left - 1:right][::-1]

        root = ListNode(tmp.pop(0))
        result_root = root
        while tmp:
            root.next = ListNode(tmp.pop(0))
            root = root.next
        return result_root


### 다른 사람 코드 ###

class Solution:
    def reverseBetween(self, head, left: int, right: int):

        if not head.next:
            return head

        curr, start = head, head

        count = 1

        while count < left:
            start = curr
            curr = curr.next
            count += 1

        tail = curr

        prev = None
        while count < right:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1

        last = curr.next
        curr.next = prev
        prev = curr

        start.next = curr
        tail.next = last

        if left > 1:
            return head

        return prev

### 책 풀이 코드 ###

class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head

        root = start = ListNode(None)
        root.next = head
        for _ in range(left-1):
            start = start.next
        end = start.next

        for _ in range(right-left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next

