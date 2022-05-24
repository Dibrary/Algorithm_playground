
# 문제 보자마자 딱 맞닥뜨린 어려움은 입력으로 트리구성을 어떻게 하느냐.
# 리프노드는 left, right가 모두 None인 노드

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right=  right
#
# n = int(input())
# arr = list(map(int, input().split()))
# target = int(input()) # 삭제 해야 하는 node
# if target == 0:
#     print(0)
# else:
#     table = dict()
#
#     root = TreeNode(arr[0])
#     table[0] = root
#     for i in range(1, n):
#         table[i] = TreeNode(i)
#         if i%2 != 0:
#             table[arr[i]].left = table[i]
#         elif i%2 == 0:
#             table[arr[i]].right = table[i]
#
#     cnt = 0
#
#     table[target] = None
#     if target%2 != 0:
#         table[arr[target]].left = None
#     elif target%2 == 0:
#         table[arr[target]].right = None
#
#     queue = [table[0]]
#     while queue:
#         node = queue.pop(0)
#         if node.left == None and node.right == None:
#             cnt += 1
#         else:
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#
#     print(cnt)

# 입력 중간에 -1이 생겨버리면 KeyError가 발생한다.
# 이진트리라는 말이 없다. 이진트리가 아닐 수도.

# class TreeNode:
#     def __init__(self, val=0):
#         self.val = val
#         self.childs = []
#
#
# n = int(input())
# arr = list(map(int, input().split()))
# target = int(input())  # 삭제 해야 하는 node
#
# if target == 0:
#     print(0)
# else:
#     table = dict()
#
#     root = TreeNode(arr[0])
#     table[0] = root
#
#     for i in range(1, n):
#         table[i] = TreeNode(i)
#
#         if i % 2 != 0 and arr[i] != -1:
#             table[arr[i]].left = table[i]
#         elif i % 2 == 0 and arr[i] != -1:
#             table[arr[i]].right = table[i]
#         elif arr[i] == -1:
#             table[0].childs.append(table[i])

# 근데 부모가 없다면 -1인 것이다. -1이면 무조건 root로 잇는 것이 아니라.


