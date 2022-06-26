'''
연결 리스트에서 중복된 요소를 제거한 리스트를 만들고, root를 반환하자.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        tmp = set()

        while head != None:
            tmp.add(head.val)
            head = head.next

        tmp = list(tmp)
        tmp.sort()

        root = None
        result_root = None
        for i in range(0, len(tmp)):
            if len(tmp) == 0:
                break
            if i == 0:
                root = ListNode(tmp.pop(0))
                result_root = root
            else:
                root.next = ListNode(tmp.pop(0))
                root = root.next

        return result_root

if __name__=="__main__":
    e = ListNode(3, None)
    d = ListNode(3, e)
    c = ListNode(2, d)
    b = ListNode(1, c)
    a = ListNode(1, b)

    k = Solution()
    v = k.deleteDuplicates(a)
    while v != None:
        print(v.val)
        v = v.next