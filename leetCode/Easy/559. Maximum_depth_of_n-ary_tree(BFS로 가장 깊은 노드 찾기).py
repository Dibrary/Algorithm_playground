
# class Solution:
#     def calc(self, root, cnt):
#
#         if root.children == None:
#             return cnt
#         else:
#             for k in root.children:
#                 self.calc(k, cnt+1)
#
#     def maxDepth(self, root):
#         result = []
#         if root.children == None:
#             return 1
#         for k in root.children:
#             result.append(self.calc(k,1))
#         print(result)
#         return max(result)

# class Solution:
#     def __init__(self):
#         self.cnt = 1
#
#     def calc(self, root, cnt):
#         if root == None:
#             return self.cnt
#         for k in root.children:
#             return self.calc(k, cnt+1)
#
#     def maxDepth(self, root):
#         if root == None:
#             return self.cnt
#         for k in root.children:
#             return self.calc(k, self.cnt+1)

from collections import deque

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        queue = deque()
        depth = 1
        queue.append((root, depth))
        while queue:
            node, depth = queue.popleft()
            if node.children:
                for child in node.children:
                    queue.append((child, depth + 1))
        return depth



class Node:
    def __init__(self,val=None, children=None):
        self.val = val
        self.children = children

a = Node(1)
b = Node(3)
c = Node(2)
d = Node(4)
e = Node(5)

a.children = [b, c, d] # 이게 다를듯.
b.children = e

k = Solution()
# print(type(a.children))
k.maxDepth(a)

# leetcode에서 나오는 에러 문구와 다름.. 입력 형식이 다른거 같은데.

# children 타입은 list다. list 안에 Node 객체가 들어있음.


