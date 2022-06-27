
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        if head == None: return None

        tmp = []

        while head:
            tmp.append(head.val)
            head = head.next
        for i in range(0, len(tmp), 2):
            if i + 1 == len(tmp):
                continue
            else:
                tmp[i], tmp[i + 1] = tmp[i + 1], tmp[i]

        root = ListNode(tmp.pop(0))
        result_root = root

        while tmp:
            root.next = ListNode(tmp.pop(0))
            root = root.next
        return result_root


### 다른 사람 코드 ###

class Solution:
    def swapPairs(self, head):

        if head == None or head.next == None:
            return head

        prev = ListNode()
        prev.next = head
        ans = head.next
        start = head

        while start != None:

            nex = start.next
            prev.next = nex
            start.next = nex.next
            nex.next = start
            prev = start
            start = start.next

            if start == None:
                return ans
            elif start.next == None:
                return ans

        return ans


## 책 풀이 ##

class Solution:
    def swapPairs(self, head):
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val # 값 교환
            cur = cur.next.next # 다다음 노드로 곧바로 이동

        return head


class Solution:
    def swapPairs(self, head):
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next
        return root.next



class Solution:
    def swapPairs(self, head):
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head