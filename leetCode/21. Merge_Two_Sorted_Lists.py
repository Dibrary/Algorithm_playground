'''
두 개의 리스트를 합치되, 오름차순으로 값이 유지되게 합해야 한다.

각 연결 리스트의 최대 길이는 50개 까지 주어진다.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        root = None
        result_root = None

        if l1 == None and l2 == None:
            return None
        elif l1 == None and l2 != None:
            return l2
        elif l1 != None and l2 == None:
            return l1

        for i in range(0, 101):
            if i == 0:
                if l1.val > l2.val:
                    root = ListNode(l2.val, None)
                    l2 = l2.next
                else:
                    root = ListNode(l1.val, None)
                    l1 = l1.next
                result_root = root

            else:
                if l1 != None and l2 != None:
                    if l1.val > l2.val:
                        root.next = ListNode(l2.val, None)
                        l2 = l2.next
                    else:
                        root.next = ListNode(l1.val, None)
                        l1 = l1.next
                elif l1 == None and l2 == None:
                    break
                elif l1 == None and l2 != None:
                    root.next = ListNode(l2.val, None)
                    l2 = l2.next
                elif l1 != None and l2 == None:
                    root.next = ListNode(l1.val, None)
                    l1 = l1.next
                root = root.next

        return result_root


if __name__ == "__main__":
    k = Solution()

    b1 = ListNode(4, None)
    a1 = ListNode(2, b1)
    l1 = ListNode(1, a1)

    b2 = ListNode(4, None)
    a2 = ListNode(3, b2)
    l2 = ListNode(1, a2)

    f = k.mergeTwoLists(None, l2)
    s = k.mergeTwoLists(l1, l2)
    while f != None:
        print(f.val)
        f = f.next

    while s != None:
        print(s.val)
        s = s.next

    