from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if head == None: return None

        even_q = deque()
        odd_q = deque()

        cnt = 0
        while head != None:
            if cnt % 2 == 0:
                even_q.append(head.val)
            else:
                odd_q.append(head.val)
            cnt += 1
            head = head.next

        root = ListNode(even_q.popleft())
        result_root = root
        while len(even_q) != 0:
            node = ListNode(even_q.popleft())
            root.next = node
            root = root.next
        try:
            root.next = ListNode(odd_q.popleft())
            root = root.next
            while len(odd_q) != 0:
                node = ListNode(odd_q.popleft())
                root.next = node
                root = root.next
            return result_root
        except:
            return result_root


### 남의 코드 ###
class Solution:
    def oddEvenList(self, head):
        if not head:
            return head

        odd, even = head, head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenHead
        return head


## 책의 코드 ##


class Solution:
    def oddEvenList(self, head):
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head
        return head