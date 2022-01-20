
class ListNode:
    def __init__(self,val =0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self,list1, a, b, list2):
        arr1 = []
        while list1:
            arr1.append(list1.val)
            list1 = list1.next
        arr2 = []
        while list2:
            arr2.append(list2.val)
            list2 = list2.next

        arr1[a:b+1] = arr2

        root = ListNode(arr1.pop(0))
        result_root = root
        while arr1:
            root.next = ListNode(arr1.pop(0))
            root = root.next
        return result_root




