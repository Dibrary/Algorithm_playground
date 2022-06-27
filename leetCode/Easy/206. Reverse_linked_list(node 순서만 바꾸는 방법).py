from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if head == None: return None

        q = deque() # 나는 모조리 node 구성요소를 순서대로 꺼내 담은 후
        while head != None:
            q.append(head.val)
            head = head.next

        root = ListNode(q.pop())
        result_root = root
        while len(q) != 0:
            root.next = ListNode(q.pop()) # 역순으로 연결했다.
            root = root.next
        return result_root


### 다른 사람 코드 ###

class Solution:
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

class Solution:
    def reverseList(self, head):
        return self.recursive(head)

    def recursive(self, head, newHead = None):
        if not head:
            return newHead
        return self.recursive(head.next, ListNode(head.val, newHead))



## 책 코드 ##

class Solution: # 재귀로 푼 것
    def reverseList(self, head):
        def reverse(node, prev):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)



class Solution: # 반복으로 푼 것
    def reverseList(self, head):
        node, prev = head, None

        while node:
            next, node.next = node.next, prev # 현재 node의 next를 next변수에 담은 뒤, node.next는 None으로 설정.
            prev, node = node, next           # 이 부분이 이해가 잘 안된다.
        return prev

