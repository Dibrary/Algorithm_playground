class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root, val):

        result_root = None
        q = []

        q.append(root)
        while q:
            node = q.pop(0)
            if node.val == val:
                result_root = node
                break
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return result_root