class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        tmp = []
        tmp.append(root)

        values = []
        while tmp:
            node = tmp.pop(0)
            values.append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)

        values.sort()

        root = TreeNode(values.pop(0))
        result_root = root
        while values:
            root.right = TreeNode(values.pop(0))
            root = root.right
        return result_root