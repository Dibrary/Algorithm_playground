
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bfs2(self, n):

        result = [n.val]

        stack = []
        stack.append(n)
        while stack:
            node = stack.pop(0)
            if node != None:
                if node.right == None:
                    result.append("N")
                elif node.right:
                    result.append(node.right.val)
                    stack.append(node.right)
                if node.left == None:
                    result.append("N")
                elif node.left:
                    result.append(node.left.val)
                    stack.append(node.left)
            else:
                result.append("N")
        return result
    def bfs(self, n):
        result = [n.val]

        stack = []
        stack.append(n)
        while stack:
            node = stack.pop(0)
            if node != None:
                if node.left == None:
                    result.append("N")
                elif node.left:
                    result.append(node.left.val)
                    stack.append(node.left)
                if node.right == None:
                    result.append("N")
                elif node.right:
                    result.append(node.right.val)
                    stack.append(node.right)
            else:
                result.append("N")
        return result

    def isSymmetric(self, root):
        a = self.bfs(root.left)
        b = self.bfs2(root.right)
        print(a,"a")
        print(b, "b")
        return a == b



e = TreeNode(3)
d = TreeNode(2)
c = TreeNode(3)
b = TreeNode(2)
a = TreeNode(1)

a.left = b
a.right = d
b.right = c
d.right = e

tmp = Solution()
print(tmp.isSymmetric(a))


## 위 코드로 하면 안 된다.

g = TreeNode(3)
f = TreeNode(4)
e = TreeNode(2)
d = TreeNode(4)
c = TreeNode(3)
b = TreeNode(2)
a = TreeNode(1)

a.left = b
a.right = e
b.left = c
b.right = d
e.left = f
e.right = g
print(tmp.isSymmetric(a))


### 위 코드는 코드 중복도 많고, 문제가 있다.








## 다른 사람 코드 ##

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isSubtreeSymmetric(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            else:
                return left.val == right.val and isSubtreeSymmetric(left.left, right.right) and isSubtreeSymmetric(
                    left.right, right.left)

        return isSubtreeSymmetric(root, root)




class Solution(object):
    def isSymmetric(self, root):
        queue = [root, root]
        while len(queue) != 0:
            left = queue.pop(0)
            right = queue.pop(0)
            if not left and not right:
                continue
            if not left or not right:
                return False
            else:
                if left.val == right.val:
                    queue.extend([left.left, right.right, left.right, right.left])
                else:
                    return False
        return True







from collections import deque
from typing import Optional

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left and root.right:
            stack1 = deque()
            stack2 = deque()
            node1 = root.left
            node2 = root.right
            while node1 or stack1 or node2 or stack2:
                if node1 and node2:
                    stack1.append(node1)
                    node1 = node1.left
                    stack2.append(node2)
                    node2 = node2.right
                elif (not node1 and not node2):
                    node1 = stack1.pop()
                    node2 = stack2.pop()
                    if node1.val != node2.val:
                        return False
                    node1 = node1.right
                    node2 = node2.left
                else:
                    return False
            return True

        elif root.left == root.right:
            return True
        return False








class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.isMirror(root.left, root.right)

    def isMirror(self, root_1, root_2):
        if root_1 is None and root_2 is None:
            return True

        if root_1 is not None and root_2 is not None:
            if root_1.val == root_2.val:
                return self.isMirror(root_1.left, root_2.right) and self.isMirror(root_1.right, root_2.left)

        return False







class Solution:
    def symm(self, p, q):
        if not p and not q:
            return True

        if p and q:
            return p.val == q.val and self.symm(p.left, q.right) and self.symm(p.right, q.left)

        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.symm(root.left, root.right)