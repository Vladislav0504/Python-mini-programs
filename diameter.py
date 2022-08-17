# Определение узла бинарного дерева.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None        

class Solution:
    def diameter(self, root: TreeNode) -> int:
        if root is None:
        	return 0
        return self.maxDepth(root.left) + self.maxDepth(root.right)
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
        	return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))