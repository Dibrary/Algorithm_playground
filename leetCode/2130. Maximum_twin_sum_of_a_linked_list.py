
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head):
        arr = [5,4,2,1]
        # while head:
        #     arr.append(head.val)
        #     head = head.next

        for i in range(len(arr)//2):
            print(arr[i], arr[-i-1])

print(Solution().pairSum("None"))