
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next

    single_values = []
    for i in values:
        if values.count(i) == 1:
            single_values.append(i)
    
    if single_values == []: return None # 중복 값으로만 이뤄져 있으면

    root = ListNode(single_values.pop(0))
    result_root = root

    while single_values:
        root.next = ListNode(single_values.pop(0))
        root = root.next
    return result_root

