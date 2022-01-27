class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head):
        values = []
        while head:
            values.append(head.val)
            head = head.next

        if values == []:
            return None
        elif len(values) == 1:
            return None

        result = []
        if len(values) == 2:
            result.append(values[0])
        else:
            tmp = len(values) // 2
            result = values[:tmp] + values[tmp + 1:]

        root = ListNode(result.pop(0))
        result_root = root
        while result:
            root.next = ListNode(result.pop(0))
            root = root.next
        return result_root
    
# 시간초과