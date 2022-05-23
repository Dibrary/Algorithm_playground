class Solution:
    def __init__(self):
        self.result = []

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return root
        else:
            if root.left:
                self.postorderTraversal(root.left)
            if root.right:
                self.postorderTraversal(root.right)
            self.result.append(root.val) # 이 넣는 순서만 바꾸면 전위, 후위, 중위 순회로 변경 가능.
        return self.result


