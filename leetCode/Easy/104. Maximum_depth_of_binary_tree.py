
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        cnt = 1

        if root == None: return 0

        q = []
        q.append((root ,cnt))

        while q:
            node, cnt = q.pop(0)
            if node == None:
                pass
            else:
                if node.left:
                    q.append((node.left, cnt +1))
                if node.right:
                    q.append((node.right, cnt +1))
        return cnt
    
# 통과