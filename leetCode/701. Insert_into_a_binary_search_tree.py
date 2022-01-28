class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root, val):
        result_root = root
        if root == None: return TreeNode(val)

        while True:
            if val <= root.val and root.left:
                root = root.left
            elif val <= root.val and root.left == None:
                root.left = TreeNode(val)
                break
            elif val > root.val and root.right:
                root = root.right
            elif val > root.val and root.right == None:
                root.right = TreeNode(val)
                break
        return result_root