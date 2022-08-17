# Определение узла бинарного дерева.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None        

class Solution:
    def hasPathSum(self, root: TreeNode, sum_val) -> bool:
        if root is None and sum_val == 0:
        	return True
        elif root is None:
        	return False
        return self.hasPathSum(root.left, sum_val - root.val) or self.hasPathSum(root.right, sum_val - root.val)