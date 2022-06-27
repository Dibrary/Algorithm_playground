

class Solution:
    def isPalindrome(self, head):
        arr = []
        
        while head: # 요소 전부 뽑아다가 list에 넣는 코드
            arr.append(head.val)
            head = head.next

        # if arr == arr[::-1]:
        #     return True
        # else:
        #     return False

        return arr == arr[::-1] # 이렇게 간단하게 할 수 있다.


### 책 코드 ###

class Solution:
    def isPalindrome(self, head):
        q = []
        # [] 대신에 deque() 를 써도 된다. 대신 pop(0)이 popleft()로 바뀌어야됨.

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) >1:
            if q.pop(0) != q.pop():
                return False

        return True



## 아래 코드도 책 코드 ##
# 자주 쓰지 않았던 코드 표현 방식을 눈여겨보자.

class Solution:
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next # 다중할당
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev


