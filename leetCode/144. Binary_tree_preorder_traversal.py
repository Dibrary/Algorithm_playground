# class Solution:
#     def __init__(self):
#         self.result = []
#
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root == None:
#             self.result.append(None) # 여기서 에러 남. 입력이 None일 경우 처리가 안됨.
#         else:
#             self.result.append(root.val)
#             if root.left:
#                 self.preorderTraversal(root.left)
#             if root.right:
#                 self.preorderTraversal(root.right)
#         return self.result


class Solution:
    def __init__(self):
        self.result = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return root # 이렇게 수정하니까 됨.
        else:
            self.result.append(root.val)
            if root.left:
                self.preorderTraversal(root.left)
            if root.right:
                self.preorderTraversal(root.right)
        return self.result