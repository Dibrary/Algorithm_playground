'''
2개의 연결리스트로 된 값이 있다.
이들 값을 뒤집은 후에, 더한 해당값을 리스트로 만들어 반환하자.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):

        lr1, lr2 = '', ''

        root = l1
        while root != None:
            lr1 += str(root.val)
            root = root.next

        root = l2
        while root != None:
            lr2 += str(root.val)
            root = root.next

        lr1, lr2 = lr1[::-1], lr2[::-1]
        # return [int(x) for x in str(int(lr1) + int(lr2))[::-1]] # 단순히 list 모양만 반환할 거면 이렇게,
        sum_value = [int(x) for x in str(int(lr1) + int(lr2))[::-1]]

        root = None
        result_root = None
        for i in range(0, len(sum_value)):
            if i == 0:
                root = ListNode(sum_value.pop(0))
                result_root = root
            else:
                root.next = ListNode(sum_value.pop(0))
                root = root.next

        return result_root # list를 만들고, 해당 list의 첫 번째 node를 반환.


if __name__=="__main__":

    c1 = ListNode(4, None)
    b1 = ListNode(6, c1)
    a1 = ListNode(5, b1)

    c2 = ListNode(8, None)
    b2 = ListNode(0, c2)
    a2 = ListNode(7, b2)

    k = Solution()
    print(k.addTwoNumbers(a2, a1))





### 책 풀이 ###

class Solution:
    def reverseList(self, head):
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    def toList(self, node):
        list = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    def toReversedLinkedList(self, result):
        prev: ListNode = None

        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

        return node

    def addTwoNumbers(self, l1, l2):
        a = self.toList(self.reverseList(l1)) # node값을 일일이 list로 담아서 꺼낸다.
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b)) # 하나의 문자열로 바꾸고 숫자로 변경해서 합친다.

        return self.toReversedLinkedList(str(resultStr)) # 해당 합친 list값 하나하나 node를 구성해서 연결한다.



### 다른 풀이 ###

def addTwoNumbers(self, l1, l2):
    root = head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        sum = 0
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        carry, val = divmod(sum+carry, 10) # 연산 결과로 몫은 자리 올림수 형태로 사용
        head.next = ListNode(val)
        head = head.next

    return root.next
