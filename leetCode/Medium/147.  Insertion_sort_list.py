
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        values.sort()

        root = ListNode(values.pop(0))
        result_root = root
        while values:
            root.next = ListNode(values.pop(0))
            root = root.next
        return result_root


### 다른 사람 코드 ###
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []

        cur = ans = head
        while head:
            nums.append(head.val)
            head = head.next

        nums = sorted(nums)

        count = 0
        while cur:
            cur.val = nums[count]
            count += 1
            cur = cur.next

        return ans






class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        record= []
        while ptr != None:
            record.append(ptr.val)
            ptr = ptr.next
        record.sort()
        ptr = head
        count = 0
        while ptr != None:
            ptr.val = record[count]
            count += 1
            ptr = ptr.next
        return head





### 책 풀이 ###

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(None)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            cur = parent
        return cur.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 초기값 변경
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            # 필요한 경우에만 cur 포인터가 되돌아가도록 처리
            if head and cur.val > head.val:
                cur = parent
        return parent.next

