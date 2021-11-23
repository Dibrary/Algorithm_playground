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










