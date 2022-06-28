
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        tmp = []

        for i in lists:
            root = i
            while root:
                tmp.append(root.val)
                root = root.next

        if tmp == []: return None
        tmp.sort()
        root = ListNode(tmp.pop(0))
        result_root = root
        while tmp:
            root.next = ListNode(tmp.pop(0))
            root = root.next
        return result_root


### 다른 사람 풀이 ###

class Solution:
    def mergeKLists(self, lists):
        lst = []
        for i in lists:
            while i:
                lst.append(i)
                i = i.next
        if len(lst) == 0: return None
        lst.sort(key=lambda x: x.val)
        l2 = lst[0]
        l2_ret = l2

        for i in range(1, len(lst)):
            # print(l2.val)
            l2.next = lst[i]
            l2 = l2.next
        l2.next = None

        return l2_ret

### 책 풀이 ###

from collection import heapq

class Solution:
    def mergeKLists(self, lists):
        root = result = ListNode(None)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next

            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
        return root.next


