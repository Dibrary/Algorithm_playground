
class Solution:
    def __init__(self):
        self.result = []

    def inorderTraversal(self, root):
        if root == None:
            return root # 이렇게 수정하니까 됨.
        else:
            if root.left:
                self.inorderTraversal(root.left)
            self.result.append(root.val)
            if root.right:
                self.inorderTraversal(root.right)
        return self.result