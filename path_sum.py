# Определение узла бинарного дерева.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None        

class Solution:
	def hasPathSum(self, root: TreeNode, sum_val) -> bool:
		if root is None:
			return False
		sum_val -= root.val
		return self.hasPathSum(root.left, sum_val) + self.hasPathSum(root.right, sum_val) + (sum_val == 0)
	def pathSum(self, root: TreeNode, sum_val) -> int:
		if root is None:
			return 0
		return self.pathSum(root.left, sum_val) + self.pathSum(root.right, sum_val) + self.hasPathSum(root, sum_val)