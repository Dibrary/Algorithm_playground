

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


